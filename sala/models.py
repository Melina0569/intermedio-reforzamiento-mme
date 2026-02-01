from django.db import models

# Create your models here.

class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()