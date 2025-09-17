from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = model.ForeignKey( User, on_delete=model.CASCADE)
    title= model.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
