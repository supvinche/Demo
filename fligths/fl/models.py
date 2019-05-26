from django.db import models

class Filgth(models.Model):
    origin = models.CharField(max_length = 64)# Create your models here.
    destination = models.CharField(max_length = 64)
    duration = models.IntegerField()
