from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=60000)
    time = models.CharField(max_length=30)
    typeId = models.IntegerField()
    typeIdName = models.CharField(max_length=30)
    readNum = models.IntegerField(null=True, default=0)
    commentNum = models.IntegerField(null=True, default=0)
    isPublish = models.IntegerField(default=0)