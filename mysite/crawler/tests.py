from django.test import TestCase


# Create your tests here.
# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.

class SearchRecord:
    PROXY_ITEMS = [
        (1, "Yes"),
        (0, "No"),
    ]
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="created_time")
    content_string = models.CharField(max_length=1024, verbose_name="raw_string")
    proxy = models.IntegerField(choices=PROXY_ITEMS, default=1, verbose_name="proxy")

    class Meta:
        verbose_name = verbose_name_plural = "SearchRecord"

s=SearchRecord()
s.created_time="2019/8/1 12:00:00"
print(str(s.created_time))