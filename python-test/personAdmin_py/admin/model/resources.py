from django.db import models

# Create your models here.

class Resources(models.Model):
    typeId = models.IntegerField()
    typeIdName = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)