# -*- coding: utf-8 -*-
#DRF框架演示功能
# @Author  : joker
# @Date    : 2019-01-18
from rest_framework.routers import DefaultRouter

from books import views

app_name = "books"

urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view(),name='books'),
    #
    # url(r'^books/(?P<pk>\d+)$',views.BookDetailView.as_view(),name='books_detail')
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('books', views.BookInfoViewSet,base_name = "books")  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
