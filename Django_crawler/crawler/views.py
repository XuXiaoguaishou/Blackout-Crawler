from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SearchRecordForm
from .models import SearchRecord
from django.urls import reverse
# Create your views here.


def search_page(request):
    #searchRecords = SearchRecord.objects.all()
    if request.method == 'GET':
        form = SearchRecordForm()
        context = {
            'form': form,
        }
        return render(request, 'search_page.html', context=context)

    if request.method == 'POST':
        form = SearchRecordForm(request.POST)
        a = request.POST
        print(request.POST)
        #form.save()
        #print(form.content_string)
        #print(form.created_time)
        form.save()
        return HttpResponseRedirect(reverse('crawler:search_page'))



