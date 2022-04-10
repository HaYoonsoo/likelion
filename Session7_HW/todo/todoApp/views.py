from django.shortcuts import render
from .models import Task
from datetime import date

# Create your views here.
def home(request):
    task_w_dday = Task.objects.order_by('date')

    for task in task_w_dday:
        task.dday = (task.date - date.today()).days

    return render(request, 'home.html', {'tasks': task_w_dday})