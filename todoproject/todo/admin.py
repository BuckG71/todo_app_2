from django.contrib import admin
from todo.models import *

# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)