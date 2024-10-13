from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Expense(models.Model):
    text = models.CharField(max_length=511)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)


class InCome(models.Model):
    text = models.CharField(max_length=511)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

