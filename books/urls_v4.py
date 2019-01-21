# -*- coding: utf-8 -*-
#DRF框架演示功能
# @Author  : joker
# @Date    : 2019-01-18
from django.conf.urls import url

from books import views_v4

app_name = "books"

urlpatterns = [
    url(r'^books/$', views_v4.BookListView.as_view(), name='books'),

    url(r'^books/(?P<pk>\d+)$', views_v4.BookDetailView.as_view(), name='books_detail')
]

