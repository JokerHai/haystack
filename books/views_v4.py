# -*- coding: utf-8 -*-
#使ApiView改写RestApi接口
# @Author  : joker
"""
    DRF ApiView 详解：

    什么是DRF APIView

    DRF ApiView 是view类的子类，在View类的基础上添加了一些额外的功能


    DRF框架ApiView都有哪些功能

    1:视图中request对象不再是django原始的

        HttpRequest类的对象，而是有DRF框架封装成的Request类的对象

    2:相应时可以统一返回request类的对象

    3:异常处理 如果视图中抛出了未处理异常，DRF框架会自动对异常进行处理，并且把处理之后的错误信息返回给客户端

    Request类的对象 由 request.data 获取，参数由request.query.params


    Response类的对象， 传入原始的响应数据，会自动根据客户的请求头中`Accept`将响应数据转换为对应的格式进行返回，默认返回json，仅支持json和html

"""
# @Date    : 2019-01-18

from django.http import JsonResponse


from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response



from books.models import BookInfo
from books.serializers import BookInfoSerialize


class BookListView(GenericAPIView):

    #指定当前视图所使用的序列化器类
    serializer_class = BookInfoSerialize

    queryset = BookInfo.objects.all()

    #查询所有的图书
    def get(self,request):

        queryset = self.get_queryset() #QuerySet

        serializer = BookInfoSerialize(queryset,many=True)

        return Response(serializer.data)
    #新增图书
    def post(self,request):

        #反序列-数据校验

        un_serializer = BookInfoSerialize(data=request.data)

        un_serializer.is_valid(raise_exception=True) #校验失败直接报错

        #反序列化-数据保存

        un_serializer.save()

        return Response(un_serializer.data,status=status.HTTP_201_CREATED)

class BookDetailView(GenericAPIView):

    serializer_class = BookInfoSerialize

    queryset = BookInfo.objects.all()

    #查看单个图书信息

    def get(self,request,pk):

        books = self.get_object()

        serializer = self.get_serializer(books)

        return Response(serializer.data)

    #修改图书信息
    def put(self,request,pk):

        #获取books 实例
        books = self.get_object()

        #反序列-数据效验
        un_serializer = self.get_serializer(books,request.data)

        #数据保存
        un_serializer.save()

        return Response(un_serializer.data)

    #删除图书信息
    def delete(self,request,pk):

        books = self.get_object()

        books.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)