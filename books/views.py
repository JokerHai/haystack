# Create your views here.
import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.viewsets import ModelViewSet

from books.models import BookInfo
from books.serializers import BookInfoSerialize

class BookListView(View):

    #查询所有的图书
    def get(self,request):
        queryset = BookInfo.objects.all()

        serializer = BookInfoSerialize(queryset,many=True)

        return JsonResponse(serializer.data,safe = False)
    #新增图书
    def post(self,request):
        #获取json的原始数据
        request_dict = json.loads(request.body.decode())

        #反序列-数据校验

        un_serializer = BookInfoSerialize(data=request_dict)

        un_serializer.is_valid(raise_exception=True) #校验失败直接报错

        #反序列化-数据保存

        un_serializer.save()

        return JsonResponse(un_serializer.data,status=201)

class BookDetailView(View):

    #查看单个图书信息

    def get(self,request,pk):

        books = get_object_or_404(BookInfo,pk)

        serializer = BookInfoSerialize(books)

        return JsonResponse(serializer.data)

    #修改图书信息
    def put(self,request,pk):

        #获取json数据
        request_dict = json.loads(request.body.decode())

        #获取books 实例
        books = get_object_or_404(BookInfo,pk)

        #反序列-数据效验
        un_serializer = BookInfoSerialize(books,request_dict)

        #数据保存
        un_serializer.save()

        return JsonResponse(un_serializer.data)

    #删除图书信息
    def delete(self,request,pk):

        books = get_object_or_404(BookInfo,pk)

        books.delete()

        return HttpResponse(status = 204)

class BookInfoViewSet(ModelViewSet):

    queryset = BookInfo.objects.all()

    serializer_class = BookInfoSerialize