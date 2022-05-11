from django.shortcuts import render, redirect

from django.views import View

from todo.forms import TaskForm, TagForm, CommentForm
from todo.models import Task, Comment, Tag

# Create your views here.

class TodoListView(View):
    def get(self, request):
        '''GET the todo list homepage, listing all tasks in reverse order that they were created'''
        incomplete_tasks = Task.objects.filter(completed=False)
        complete_tasks = Task.objects.filter(completed=True)
        task_form = TaskForm()

        return render(
            request=request,
            template_name='list.html',
            context={
                'incomplete_tasks': incomplete_tasks,
                'complete_tasks': complete_tasks,
                'task_form': task_form
            },
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
        task_object = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task_object)

        comments = Comment.objects.filter(task=task_object).order_by('-created_at')
        comment_form = CommentForm(task=task_object)

        tags = task_object.tags.all()  # Tag.objects.filter(task=task)
        tag_form = TagForm(task=task_object)

        return render(
            request=request,
            template_name='detail.html',
            context={
                'task_form': task_form,
                'id': task_id,
                'comments': comments,
                'tags': tags,
                'comment_form': comment_form,
                'tag_form': tag_form,
            }
        )

    def post(self, request, task_id):
        '''Update or delete the specific task based on what the user submitted in the form'''
        task = Task.objects.get(id=task_id)     

        # Check request.POST to see which button the user clicked, and run the related logic
        if 'save_task' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()

        elif 'delete' in request.POST:
            task.delete()

        elif 'save_comment' in request.POST:
            # The user clicked the button to add a comment, not update the task
            comment_form = CommentForm(request.POST, task=task)
            comment_form.save()

            # In this case, we don't want to go back to the homepage, reload the 
            # current page instead
            return redirect('task', task_id=task.id)

        elif 'add_tag' in request.POST:
            tag_form = TagForm(request.POST, task=task)
            tag_form.save()

            return redirect('task', task_id=task.id)

        elif 'complete' in request.POST:
            task.completed = True
            task.save()

        # "redirect" to the todo homepage
        return redirect('todo_list')
