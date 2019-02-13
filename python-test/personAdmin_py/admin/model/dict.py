from django.db import models

# Create your models here.

class Dict(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    typeId = models.IntegerField()






class DictType(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField(null=True, default=0)