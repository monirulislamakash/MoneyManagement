from django.db import models
from datetime import date
# Create your models here.
class Debit(models.Model):
    Head_Name=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)
    Date=models.DateField(date.today(),default=date.today())
    Expans_type=models.CharField(max_length=150,default="")
    Vaucher=models.CharField(max_length=200,default="")
    def __str__(self):
        return str(self.Head_Name)
class Credit(models.Model):
    Head_Name=models.CharField(max_length=100)
    Amount=models.CharField(max_length=100)
    Date=models.DateField(date.today(),default=date.today())
    Expans_type=models.CharField(max_length=150,default="")
    Vaucher=models.CharField(max_length=200,default="")
    def __str__(self):
        return str(self.Head_Name)
class Opaning(models.Model):
    Date=models.DateField(date.today(),default=date.today())
    Opaning=models.IntegerField()
    def __str__(self):
        return str(self.Date)
class Closing(models.Model):
    Date=models.DateField(date.today(),default=date.today())
    Closing=models.CharField(max_length=100)
    def __str__(self):
        return str(self.Date)