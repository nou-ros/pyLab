from django.db import models
from datetime import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    task_created = models.DateTimeField(default=datetime.now, blank=True)
    task_completed = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title