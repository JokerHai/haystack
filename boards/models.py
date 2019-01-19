from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#板块模型
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True,verbose_name='板块名称')
    description = models.CharField(max_length=100,verbose_name='板块描述')


    def __str__(self):

        return self.name

#主题表
class Topic(models.Model):
    subject = models.CharField(max_length=255,verbose_name='主题内容')
    last_updated = models.DateTimeField(auto_now_add=True,verbose_name='话题的排序') #auto_now_add= true 告诉django对象时间为当前时间
    board = models.ForeignKey(Board, related_name='topics',verbose_name='外键')#一个Topic实例涉及到board 实例
    starter = models.ForeignKey(User, related_name='topics',verbose_name='发起人')

#帖子
class Post(models.Model):
    message = models.TextField(max_length=4000,verbose_name='内容')
    topic = models.ForeignKey(Topic, related_name='posts',verbose_name='外键主题')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated_at = models.DateTimeField(null=True,verbose_name='更新时间')
    created_by = models.ForeignKey(User, related_name='posts',verbose_name='外键字段')#关联的User模型,谁创建的帖子
    updated_by = models.ForeignKey(User, null=True, related_name='+',verbose_name='外键字段')#related_name='+'。这指示Django我们不需要这种反向关系
