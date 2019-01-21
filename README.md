django 初学者 案例


使用步骤：

        python -m venv venv

        . venv/bin/activate 进入虚拟环境

        pip install -r requirements.txt 导入jar 依赖包


        使用数据迁移命令创建数据库

            生成迁移文件

            python manage.py makemigrations

            同步到数据库中

            python manage.py migrate

        注意：
                数据库配置文件需要更改，请查看数据库配置的是否相同

DRF框架学习总结

APIView：View类的子类，在View类的基础上添加了一些功能。

	​	1）request对象是由DRF框架封装成Request类的对象。

	​	request.data：解析之后的请求体的数据。request.body|request.POST|request.FILES

	​	request.query_params：解析之后的查询字符串的数据。

	​	2）响应可以统一返回Response的对象。

	​		Accept json html

	​	3）异常。

	​	4）高级功能：认证 权限 限流

​

GenericAPIView：APIView类的子类，在APIView类的基础上添加操作序列化器和数据库查询的相关方法。

操作序列化器：

	​	属性：serializer_class：指定视图所使用的序列化器类

	​	方法：

	​		get_serializer_class：返回视图所使用的序列化器类

	​		get_serializer：创建序列化器类的对象

数据库查询：

	​	属性：queryset：指定视图所使用的查询集。

	​	方法：

	​		get_queryset：获取视图所使用的查询集。

	​		get_object：从视图所使用的查询集中获取指定的对象，默认根据pk进行查询。



##### 视图类

```python
# 需求1：写一个类视图，提供以下1个接口
	1. 获取所有的图书数据 get /books/
    # 子类视图版本
    class BookListView(ListAPIView):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer

    # APIView版本
    class BookListView(APIView):
        def get(self, request):
            # 1. 获取所有的图书的数据
            books = BookInfo.objects.all()

            # 2. 将图书数据序列化并返回
            serializer = BookInfoSerializer(books, many=True)
           	return Response(serializer.data)

    # GenericAPIView版本
    class BookListView(GenericAPIView):
        serializer_class = BookInfoSerializer
        queryset = BookInfo.objects.all()

        def get(self, request):
            # 1. 获取所有的图书的数据
            books = self.get_queryset()

            # 2. 将图书数据序列化并返回
            serializer = self.get_serializer(books, many=True)
            return Response(serializer.data)

    # Mixin扩展类版本
    class BookListView(ListModelMixin,
                       GenericAPIView):
        serializer_class = BookInfoSerializer
        queryset = BookInfo.objects.all()

        def get(self, request):
            return self.list(request)


# 需求2：写一个类视图，提供以下2个接口
	1. 获取指定的图书数据 get /books/(?P<pk>\d+)/
    2. 修改指定的图书数据 put /books/(?P<pk>\d+)/
    #  子类视图版本
    class BookDetailView(RetrieveUpdateAPIView):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer

   	# APIView版本
	class BookDetailView(APIView):
        def get(self, request, pk):
            try:
                book = BookInfo.objects.get(pk=pk)
            except BookInfo.DoesNotExist:
                raise Http404

           	serializer = BookInfoSerializer(book)
            return Response(serializer.data)


        def put(self, request, pk):
            try:
                book = BookInfo.objects.get(pk=pk)
            except BookInfo.DoesNotExist:
                raise Http404

           	serializer = BookInfoSerializer(book, data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save() # update

            return Response(serializer.data)

    # GenericAPIView版本
    class BookDetailView(GenericAPIView):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer

        def get(self, request, pk):
            book = self.get_object()

           	serializer = self.get_serializer(book)
            return Response(serializer.data)


        def put(self, request, pk):
            book = self.get_object()

           	serializer = self.get_serializer(book, data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save() # update

            return Response(serializer.data)

	# Mixin扩展类版本
   	class BookDetailView(RetrieveModelMixin,
                        UpdateModelMixin,
                        GenericAPIView):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer

        def get(self, request, pk):
            return self.retrieve(request)


        def put(self, request, pk):
            return self.update(request)
```

##### 视图集

```python
# 需求1：写一个视图集，提供以下两种操作
	1. 获取一组图书信息(list) GET /books/
    2. 新建一本图书信息(create) POST /books/
    class BookInfoViewSet(ListModelMixin,
                          CreateModelMixin,
                          GenericViewSet):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer


# 需求2：写一个视图集，提供以下两种操作
	1. 获取一组图书信息(list) GET /books/
    2. 获取指定图书信息(retrieve) GET /books/(?P<pk>\d+)/
    class BookInfoViewSet(ReadOnlyModelViewSet):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer

# 需求3：写一个视图集，提供以下三种操作
	1. 获取一组图书信息(list) GET /books/
    2. 获取指定图书信息(retrieve) GET /books/(?P<pk>\d+)/
    3. 更新指定图书信息(update) PUT /books/(?P<pk>\d+)/
    class BookInfoViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
        queryset = BookInfo.objects.all()
        serializer_class = BookInfoSerializer
```





##### 类视图

APIView：

	​	1）request对象是Request类的对象

	​		request.data：解析之后请求体的数据。request.body, request.POST, request.FILES

	​		request.query_params: 解析之后的查询字符串数据。

	​	2）统一返回Response对象

	​	3）异常处理

	​	4）高级功能：认证 权限 限流



GenericAPIView：APIView类子类

操作序列化器：

	​	属性：serializer_class：指定当前视图所使用的序列化器类

	​	方法：

	​			get_serializer_class：返回当前视图所使用的序列化器类

	​			get_serializer：创建一个视图所使用的序列化器类的对象

数据库查询：

	​	属性：queryset：指定当前视图所使用的查询集

	​	方法：

	​		get_queryset：获取当前视图所使用的查询集

	​		get_object：从查询集中查询指定的对象，默认根据pk进行查询

其他功能：过滤 分页



Mixin扩展类：5个

	​	ListModelMixin： list

	​	CreateModelMixin：create

	​	RetrieveModelMixin：retrieve

	​	UpdateModelMixin：update

	​	DestroyModelMixin：destroy



子类视图：9个

	​	ListCreateAPIView：	GenericAPIView，ListModelMixin，CreateModelMixin，get， post



##### 视图集

1）视图集基本使用

	​	继承父类：ViewSet GenericViewSet ModelViewSet ReadOnlyModelViewSet

	​	视图集中处理函数以对应操作命名：list create retrieve update destroy

	​	进行url地址配置时需要指明请求方式和视图集中处理函数之间的对应关系









