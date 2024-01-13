from django.db import models
from .choices import StatusChoice
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=StatusChoice.CHOICE_LIST, max_length=20)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    is_important = models.BooleanField(default=False)
    due_date = models.DateField()
    due_time = models.TimeField()
    tag = models.ManyToManyField(Tag, related_name='tasks', through='TaskTag')

    def __str__(self) -> str:
        return self.title

class TaskTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['tag_id', 'task_id'],
                name='unique_task_tag'
            )
        ]

    def __str__(self) -> str:
        return str(self.tag_id) + "-" + str(self.task_id)