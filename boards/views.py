from django.contrib.auth.models import User

from boards.forms import NewTopicForm
from .models import Board, Topic, Post
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.


def home(request):

    boards = Board.objects.all()

    return render(request, 'board/home.html', {'boards':boards})



def board_topics(request,pk):

    board = get_object_or_404(Board,pk=pk)

    return render(request, 'board/topics.html', {'board':board})



def new_topic(request,pk):

    board = get_object_or_404(Board,pk=pk)

    user = User.objects.first()  # TODO 临时使用一个账号作为登录用户

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('boards:board_topics',pk = board.pk) #TODO 重定向到创建的主题页
    else:
        form = NewTopicForm()
    return render(request, 'board/new_topic.html', {'board':board, 'form':form})


