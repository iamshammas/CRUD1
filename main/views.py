from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
# Create your views here.

def home(request):
    task = Task.objects.filter(is_completed=False)
    complete = Task.objects.filter(is_completed=True)
    context = {
        'task': task,
        'complete': complete
    }
    return render(request, 'home.html',context)

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        Task.objects.create(title=title)
    return redirect('home')

def mark_as_done(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('home')

def update_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('new_task')
        task.save()
        print(request.POST)
        return redirect('home')
    context = {
        'get_task': task,
    }
    return render(request,'update.html',context)