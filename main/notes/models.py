from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length=500)
    def __str__(self):
        return f'{self.title}'