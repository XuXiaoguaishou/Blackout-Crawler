from django.test import TestCase,Client
from .models import Student

# Create your tests here.


class StudentTestCase(TestCase):
    def setUp(self) -> None:
        Student.objects.create(
            name='the5fier',
            sex=1,
            email='xgs@dlf.com',
            profession='coder',
            qq='3333',
            phone='32222',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='the5fir',
            sex=1,
            email='xgs@dlf.com',
            profession='coder',
            qq='3333',
            phone='32222',
        )
        self.assertEqual(student.sex_show, 'male', 'did not match')

    def test_filter(self):
        Student.objects.create(
            name='the5fr',
            sex=1,
            email='xgs@dlf.com',
            profession='coder',
            qq='3333',
            phone='32222',
        )
        name = 'the5fier'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, 'there should be on record called {}'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')
        # test the aviliablity of homepage

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='xgs@dlf.com',
            profession='coder',
            qq='3333',
            phone='32222',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.contentm,
                        'response conteen must contain “test_for_post”')