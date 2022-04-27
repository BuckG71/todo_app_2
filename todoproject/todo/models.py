from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=False)
class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
class Comment(models.Model):
    body = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

