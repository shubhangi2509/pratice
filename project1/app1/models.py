from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=30)
    sal = models.FloatField()
    age = models.IntegerField()