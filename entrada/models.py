# entrada/models.py
from django.db import models
from funcion.models import Funcion  # importa el modelo de la otra app

class Entrada(models.Model):
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)  # FK
    codigo = models.CharField(max_length=10, default='E000')
    asiento = models.CharField(max_length=5)
    vendido = models.BooleanField(default=False)
    fecha_venta = models.DateTimeField(null=True, blank=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.codigo} - {self.asiento}"