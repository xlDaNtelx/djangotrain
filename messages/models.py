from django.db import models


# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=64)
    description = models.IntegerField()
    count = models.TextField()
