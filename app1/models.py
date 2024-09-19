from django.db import models
from django.contrib.auth.models import User


class Workspace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    member1 = models.CharField(max_length=100, default='member1')
    member2 = models.CharField(max_length=100, default='member2')
    member3 = models.CharField(max_length=100, default='member3')
    member4 = models.CharField(max_length=100, default='member4')
    
    def __str__(self):
        return self.name
