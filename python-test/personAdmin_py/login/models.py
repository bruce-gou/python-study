from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    role = models.IntegerField()
    roleName = models.CharField(max_length=10)
    isEnable = models.IntegerField()
    tel = models.CharField(max_length=15, null=True)
    mailbox = models.CharField(max_length=30, null=True)

    #def __str__(self):
    #    return self.name






