from django.db import models

# Create your models here.

class Speech(models.Model):
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=3000)
    time = models.CharField(max_length=30)
    essayId = models.IntegerField()
    isCheck = models.IntegerField(null=True, default=0)