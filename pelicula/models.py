from django.db import models
from rest_framework import serializers

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    clasificacion = models.CharField(max_length=20)
    duracion_min = models.IntegerField(default=0)


    GENEROS = [
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('fantasia', 'Fantasía'),
        ('romance', 'Romance'),
        ('suspenso', 'Suspenso'),
        ('aventura', 'Aventura'),
    ]
    genero = models.CharField(max_length=20, choices=GENEROS, default='accion')


class Funcion(models.Model):
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        related_name="funciones_pelicula"
    )
    estado = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.pelicula.titulo} - {self.fecha_hora}"

class SnackCompra(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre