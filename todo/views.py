from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            if request.user.is_authenticated:
                new_task = Task(title=title, user=request.user)
                new_task.save()
            else:
                # можно перенаправить неавторизованного пользователя на вход
                return redirect('login')
        return redirect('task_list')

    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.none()

    return render(request, 'todo/task_list.html', {'tasks': tasks})
