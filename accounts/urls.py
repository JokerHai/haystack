# -*- coding: utf-8 -*-
#accounts配置项
# @Author  : joker
# @Date    : 2019-01-19
from django.conf.urls import url
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^signup/$',accounts_views.signup,name='signup'),

    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),

    url(r'^login/$',auth_views.LoginView.as_view(template_name = 'accounts/login.html'),name='login')



]