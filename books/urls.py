# -*- coding: utf-8 -*-
#DRF框架演示功能
# @Author  : joker
# @Date    : 2019-01-18
from django.conf.urls import url

from books import views

app_name = "books"

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view(),name='books'),

    url(r'^books/(?P<pk>\d+)$',views.BookDetailView.as_view(),name='books_detail')
]

