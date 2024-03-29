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

    # key_list = []   #在view层处理？


'''    def handle_raw_string(self):
        key_list

    def __str__(self):
        return self.content_string
'''


class Key:
    LANGUAGE_ITEMS = [
        (0, "CN"),
        (1, "EN"),
        (2, "empty")
    ]
    search_record = models.ForeignKey(SearchRecord, verbose_name="search_record")
    key = models.CharField(max_length=128, verbose_name="key")
    language = models.IntegerField(choices=LANGUAGE_ITEMS, default=0, verbose_name="language")

    class Meta:
        verbose_name = verbose_name_plural = "Key"


class Article:
    ADOPTED_ITEMS = [
        (1, "Yes"),
        (0, "No"),
    ]
    url = models.CharField(max_length=1024, verbose_name="url")
    original_site = models.CharField(max_length=128, verbose_name="original_site")
    content_article = models.TextField(verbose_name="content_article")
    key_id = models.ForeignKey(Key, verbose_name="key_id")
    adopted = models.IntegerField(choices=ADOPTED_ITEMS, default=1, verbose_name="language")
    title = models.CharField(max_length=1024, verbose_name="title")
    pub_data = models.DateTimeField(verbose_name="pub_time")
    image = models.ImageField(verbose_name="image")

    class Meta:
        verbose_name = verbose_name_plural = "Article"
