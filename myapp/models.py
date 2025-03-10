from django.db import models

class Counter(models.Model):
    count = models.IntegerField(default=0)

class Greeting(models.Model):
    name = models.CharField(max_length=200, default='Unknown')
    timestamp = models.DateTimeField(auto_now=True)
    greeting = models.CharField(max_length=200, default="")
