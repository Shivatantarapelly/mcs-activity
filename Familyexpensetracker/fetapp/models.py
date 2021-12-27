import django
from django.db import models
from datetime import datetime


# Create your models here.

class Add_New_Expenses(models.Model):
    Eid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Purpose = models.CharField(max_length=100)
    Amount = models.IntegerField(default=0)
    Date = models.DateTimeField("date published", default=django.utils.timezone.now)


class Add_new_member(models.Model):
    Mid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Mobile_no = models.BigIntegerField()
    Work = models.CharField(max_length=20)
    Income = models.IntegerField()
