from django import forms

from todo.models import *
# class TaskForm(forms.Form):
#     description = forms.CharField(label='Add task', max_length=255)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['description'].label = 'Add Task'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].label = 'Add Comment'