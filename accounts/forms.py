# -*- coding: utf-8 -*-
#用户注册forms表点验证
# @Author  : joker
# @Date    : 2019-01-19
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(
            max_length=254,
            required=True,
            widget=forms.EmailInput(),
            label= '邮箱'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
