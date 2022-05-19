from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

def listView(request):
  return render(request, 'blogApp/listView.html', {'posts': Post.objects.all()})

@login_required(login_url="loginView")
def createView(request):
  if request.method == 'POST':
    new_post = Post.objects.create(
      title = request.POST['title'],
      author = request.user,
      content = request.POST['content'],
    )
    return redirect('detailView', new_post.pk)
  return render(request, 'blogApp/createView.html')

@login_required(login_url="loginView")
def detailView(request, pk):
  post = Post.objects.get(pk=pk)
  if request.method == 'POST':
    Comment.objects.create(
      post = post,
      content = request.POST['content'],
      author = request.user,
    )
  return render(request, 'blogApp/detailView.html', {'post': post})

@login_required(login_url="loginView")
def detailViewAdd(request, pk):
  post = Post.objects.get(pk=pk)
  post.view += 1
  post.save()
  return redirect('detailView', pk)

@login_required(login_url="loginView")
def updateView(request, pk):
  post = Post.objects.get(pk=pk)
  if request.method == 'POST':
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('detailView', pk=pk)
  return render(request, 'blogApp/updateView.html', {'post': post})

@login_required(login_url="loginView")
def deleteView(request, pk):
  post = Post.objects.get(pk=pk)
  if request.method == 'POST':
    post.delete()
    return redirect('listView')
  return render(request, 'blogApp/deleteView.html', {'post': post})


@login_required(login_url="loginView")
def deleteComment(request, pk):
  comment = Comment.objects.get(pk=pk)
  post_pk = comment.post.pk
  comment.delete()
  return redirect('detailView', post_pk)


def loginView(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
      return redirect(request.GET.get('next', 'listView'))
    error = "아이디 또는 비밀번호가 틀립니다"
    return render(request, 'blogApp/loginView.html', {'error': error})
  return render(request, 'blogApp/loginView.html')

def logout(request):
  auth.logout(request)
  return redirect('listView')

def signupView(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    found_user = User.objects.filter(username=username)
    if len(found_user):
      error = "이미 아이디가 존재합니다"
      return render(request, 'blogApp/signupView.html', {'error': error})
    new_user = User.objects.create_user(username=username, password=password)
    auth.login(request, new_user)
    return redirect('listView')
  return render(request, 'blogApp/signupView.html')