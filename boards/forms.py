# -*- coding: utf-8 -*-
#添加主题from表单
# @Author  : joker
# @Date    : 2019-01-19

from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(
        label= '主题名称',
        error_messages={
            "required":"主题名称不能为空"
        }
    )
    #设置message验证规则
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':'What is on your mind?'}
        ),
        max_length=4000,
        help_text='最大长度是4000',
        label = '描述',
        error_messages= {
            "required": "描述不能为空",
        }
    )

    class Meta:
        model = Topic

        fields = ['subject','message']
