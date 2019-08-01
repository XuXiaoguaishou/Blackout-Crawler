# -*- coding: utf-8 -*-
from django.db import models
from __future__ import unicode_literals
# Create your models here.

class Student(models.Model):
    SEX_ITEMS = [
        (1, 'male'),
        (2, 'female'),
        (0, 'unknown'),
    ]
    STATUS_ITEMS = [
        (0, 'apply'),
        (1, 'pass'),
        (2, 'refuse'),
    ]
    name = models.CharField(max_length=128, verbose_name="name")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="sex")
    profession = models.CharField(max_length=128, verbose_name="profession")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="phone_num")

    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="status")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="reated_time")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "student_info"