from django.contrib import admin
from .models import Task, TaskTag, Tag, List

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskTag)
admin.site.register(Tag)
admin.site.register(List)