from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=10, null=True)
    path = models.CharField(max_length=100)
    orderNumber = models.CharField(max_length=10)
    isEnable = models.IntegerField()
    parentId = models.IntegerField()
    allPower = models.CharField(max_length=50)