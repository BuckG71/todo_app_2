from django.db.utils import IntegrityError
from django import forms

from todo.models import Comment, Tag, Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

    # *args: list of arguments (single * is for lists, python syntax)
    # **kwargs = dictionary key word arguments (double ** is for dictionaries, python syntax)
    def __init__(self, *args, **kwargs):
        # Run the __init__ method of the class that this one inherits from (forms.ModelForm)
        # Fun fact-- this works for any method of any class being inherited!
        super().__init__(*args, **kwargs)

        self.fields['description'].label = 'Task'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def __init__(self, *args, **kwargs):
        # We send the form the keyword 'task', so we can pop that out now to use
        self.task = kwargs.pop('task', None)
        super().__init__(*args, **kwargs)

        # Every ModelForm has a self.instance, the instance of its model that we're 
        # editing, deleting, etc
        self.instance.task = self.task
        self.fields['name'].label = ''

    def save(self, *args, **kwargs):
        # Usually, calling <form>.save() will try to create a new instance of the model.
        # In this case, a tag with the given name might already exist. Use get_or_create()
        # to only create one if it does not already exist

        # Alternative Django 
        # tag, _ = Tag.objects.get_or_create(name=self.data['name'])

        try:
            tag = Tag.objects.create(name=self.data['name'])
        except IntegrityError:
            tag = Tag.objects.get(name=self.data['name'])

        # Automatically add this tag to the task, whether it is new or not
        self.task.tags.add(tag)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        task_object = kwargs.pop('task')
        super().__init__(*args, **kwargs)

        self.instance.task = task_object
        self.fields['body'].label = ''
