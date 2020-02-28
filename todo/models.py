from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    task=models.CharField(max_length=100)
    complete_by=models.DateTimeField()
    started_on=models.DateTimeField()
    description=models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.task

    