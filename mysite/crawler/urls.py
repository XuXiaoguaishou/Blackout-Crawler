from django.urls import path

from . import views

app_name = 'crawler'

urlpatterns = [
    path('', views.index, name='index'),
    path('search-form', views.search_form, name='search_form'),
    path('search', views.search, name='search')
]