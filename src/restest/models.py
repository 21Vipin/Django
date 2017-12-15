from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_desc = models.TextField(max_length=200)
    task_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name
