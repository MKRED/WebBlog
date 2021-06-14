from django.shortcuts import render, redirect
from django.contrib import auth
import random
from .models import Post, Comment
from .forms import CommentForm, AuthForm


def index(request):
    user = ''
    is_a = request.user.is_authenticated
    if is_a:
        user = request.user


    posts = Post.objects.order_by('-id')
    return render(request, 'main/index.html', {'posts': posts, 'is_a': is_a, 'user': user})

def Auth(request):
    error = ''
    is_a = request.user.is_authenticated
    if is_a:
        auth.logout(request)
        is_a = False

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('home')
        else:
            error = 'Ошибка!'


    form = AuthForm()

    Contex = {
        'form': form,
        'error': error,
        'is_a': is_a,
    }
    return render(request, 'main/login.html', Contex)

def PostDetal(request, id):
    error = ''
    user = ''

    id_p = Post.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.father_post = id_p
            form.autor = request.user
            form.save()
        else:
            error = 'Форма была неверной'

    form = CommentForm()
    comment = Comment.objects.filter(father_post=id_p.id)
    comment = comment.order_by('-id')

    is_a = request.user.is_authenticated
    if is_a:
        user = request.user
    else:
        user = ''

    Contex = {
        'posts': id_p,
        'comment': comment,
        'form': form,
        'error': error,
        'is_a': is_a,
    }
    return render(request, 'main/vive_post.html', Contex)