from django.db import models
from datetime import date
# Create your models here.
class Debit(models.Model):
    Head_Name=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)
    Date=models.DateField(date.today(),default=date.today())
    def __str__(self):
        return str(self.Head_Name)
class Credit(models.Model):
    Head_Name=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)
    Date=models.DateField(date.today(),default=date.today())
    def __str__(self):
        return str(self.Head_Name)