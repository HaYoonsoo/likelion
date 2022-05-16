from django.shortcuts import render, redirect
from .models import Post

def listView(request):
  return render(request, 'blogApp/listView.html', {'posts': Post.objects.all()})

def createView(request):
  if request.method == 'POST':
    Post.objects.create(
      title = request.POST['title'],
      content = request.POST['content'],
    )
    return redirect('listView')
  return render(request, 'blogApp/createView.html')

def detailView(request, pk):
  post = Post.objects.get(pk=pk)
  post.view += 1
  post.save()
  return render(request, 'blogApp/detailView.html', {'post': post})

def updateView(request, pk):
  post = Post.objects.get(pk=pk)
  if request.method == 'POST':
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('detailView', pk=pk)
  return render(request, 'blogApp/updateView.html', {'post': post})

def deleteView(request, pk):
  post = Post.objects.get(pk=pk)
  if request.method == 'POST':
    post.delete()
    return redirect('listView')
  return render(request, 'blogApp/deleteView.html', {'post': post})