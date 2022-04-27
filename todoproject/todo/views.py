from django.shortcuts import render, redirect
from django.views import View

from todo.models import *
from todo.forms import *

# Create your views here.

class TodoListView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        tasks = Task.objects.all().order_by('-id')
        task_form = TaskForm()

        return render(
            request=request,
            template_name='list.html',
            context={'task_list': tasks, 'task_form': task_form},
        )

    def post(self, request):
        '''POST the data in the form submitted by the user, creating a new task in the todo list'''
        form = TaskForm(request.POST)
        form.save()

        # "redirect" to the todo homepage
        return redirect('todo_list')


class TodoDetailView(View):
    def get(self, request, task_id):
        '''GET the detail view of a single task on the todo list'''
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)

        comments = Comment.objects.filter(task=task).order_by('-created_at')

        return render(
            request=request,
            template_name='detail.html',
            context={
                'task_form': task_form,
                'id': task_id,
                'comments': comments
            }
        )

    def post(self, request, task_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        task = Task.objects.filter(id=task_id)
        task_form = TaskForm(instance=task)
        
        if 'save' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()

        elif 'delete' in request.POST:
            task.delete()

        # "redirect" to the todo homepage
        return redirect('todo_list')
