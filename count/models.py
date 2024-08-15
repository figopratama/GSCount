from django.db import models

# Create your models here.

class UjiStasioner(models.Model):
    #id = models.IntegerField(primary_key=True)
    stat = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)
    crit = models.CharField(max_length=100, null=True)
