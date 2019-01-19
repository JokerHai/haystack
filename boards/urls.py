# -*- coding: utf-8 -*-
#boards urls 配置项
# @Author  : joker
# @Date    : 2019-01-18
from django.conf.urls import url

from boards import views
urlpatterns = [
    url(r'^$',views.home, name='home'),

    url(r'^boards/(?P<pk>\d+)/$',views.board_topics,name='board_topics'),

    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic')


]
