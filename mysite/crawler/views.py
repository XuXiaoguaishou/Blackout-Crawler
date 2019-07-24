from django.shortcuts import render
from .crawler_recode import crawler

from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# 表单
def search_form(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render_to_response('search_form.html')
# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)