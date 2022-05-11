from django.db import models

# Create your models here.

class Tag(models.Model):
    # unique=True will stop multiple tags from being created with the same name
    name = models.CharField(max_length=30, unique=True)


class Task(models.Model):
    # Django automatically creates an ID column on our tables unless we tell it otherwise
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    completed = models.BooleanField(default=False)


# task = Task.objects.get(description='Learn HTML!')
# print(task.tags.all())

# tag = Tag.objects.get(name='python')
# print(tag.task_set.all())

class Comment(models.Model):
    body = models.TextField()
    # ForeignKey: connects the Comment model to the Task model
    # on_delete=models.CASCADE: if the task gets deleted, we want that to 'cascade', and delete
    # all of the comments for that task
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
