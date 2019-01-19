# -*- coding: utf-8 -*-
#accounts配置项
# @Author  : joker
# @Date    : 2019-01-19
from django.conf.urls import url

from accounts import views as accounts_views

urlpatterns = [
    url(r'^signup/$',accounts_views.signup,name='signup')
]