# -*- coding: utf-8 -*-

# @Author  : joker
# @Date    : 2019-01-18
from rest_framework import serializers

from books.models import BookInfo


class BookInfoSerialize(serializers.ModelSerializer):


    """图书数据序列化器"""

    class Meta:

        model = BookInfo

        exclude = ('is_delete',) #取出不显示的字段

        extra_kwargs = {
                'bread':{
                    'min_value':0
                },
                'bcomment':{
                    'min_value':0
                },
                'bpub_date':{
                    'required':True
                }
        }



