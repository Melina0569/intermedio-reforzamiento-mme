from django.db import models
from pelicula.models import Pelicula
# Create your models here.

class Funcion(models.Model):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        related_name="funciones_funcion"
    )
    fecha_hora = models.DateTimeField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.CharField(max_length=20)

