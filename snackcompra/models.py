from django.db import models
from entrada.models import Entrada
# Create your models here.

class SnackCompra(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)