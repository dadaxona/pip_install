from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    fam = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=50)

    def __str__(self):
        return self.name
class Docs(models.Model):
    name = models.CharField(max_length=255)
    summa = models.IntegerField(max_length=20)
    summa2 = models.IntegerField(max_length=20)
    itogo = models.IntegerField(max_length=20)
