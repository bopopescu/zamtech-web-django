from django.db import models
from django.utils import timezone


class post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50, null=True, default='unknown')
    post_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200, null=True, default='untitled')
    content = models.TextField(null=True, default='blank content')

class finance(models.Model):
    id = models.AutoField(primary_key=True)
    balance = models.IntegerField(null=True)
    withdrawal = models.IntegerField(null=True)
    deposit = models.IntegerField(null=True)
    activity_date = models.DateTimeField(default=timezone.now)