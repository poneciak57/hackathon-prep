from django.shortcuts import render, redirect
from .models import TodoItem

def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todo_items': todo_items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TodoItem.objects.create(title=title)
    return redirect('index')

def delete_todo(request, todo_id):
    TodoItem.objects.filter(id=todo_id).delete()
    return redirect('index')
