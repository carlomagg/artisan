from django.db import models

# Create your models here.

class Location(models.Model):
    bwari = models.CharField(max_length=100)
    dutse = models.CharField(max_length=100)
    kubwa = models.CharField(max_length=100)
    garki = models.CharField(max_length=11)
    wuse =models.CharField(max_length=100)
    gwarinpa = models.CharField(max_length=100)
    maitama = models.CharField(max_length=100)
    apo = models.CharField(max_length=100)
    jabi = models.CharField(max_length=100)
    utako = models.CharField(max_length=100)
    wuye = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

