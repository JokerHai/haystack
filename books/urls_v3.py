# -*- coding: utf-8 -*-
#使ApiView改写RestApi接口
# @Author  : joker
# @Date    : 2019-01-18
from django.conf.urls import url

from books import views_v3

app_name = "books"

urlpatterns = [
    url(r'^books/$', views_v3.BookListView.as_view(), name='books'),

    url(r'^books/(?P<pk>\d+)$', views_v3.BookDetailView.as_view(), name='books_detail')
]
