from django.db import models

# Create your models here.

class Power(models.Model):
    menuName = models.CharField(max_length=20)
    userTypeId = models.IntegerField()
    menuId = models.IntegerField()
    power = models.CharField(max_length=50)