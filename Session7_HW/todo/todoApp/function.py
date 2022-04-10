from django.shortcuts import redirect
from datetime import datetime
from .models import Task

def new(request):
    if request.method == 'POST':
        Task.objects.create(
            title = request.POST['title'],
            detail = request.POST['detail'],
            date = request.POST['date'],
            date_str = request.POST['date'],
        )
    return redirect('home')

def edit(request, pk):
    if request.method == 'POST':
        Task.objects.filter(pk=pk).update(
            title = request.POST['title'],
            detail = request.POST['detail'],
            date = request.POST['date'],
            date_str = request.POST['date'],
        )
    return redirect('home')

def delete(request, pk):
    Task.objects.get(pk=pk).delete()
    return redirect('home')