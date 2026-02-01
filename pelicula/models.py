from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField()  # minutos
    clasificacion = models.CharField(max_length=20)

    # Nuevo campo genero con opciones
    GENEROS = [
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror'),
        ('fantasia', 'Fantasía'),
        ('romance', 'Romance'),
        ('suspenso', 'Suspenso'),
    ]
    genero = models.CharField(max_length=20, choices=GENEROS, default='accion')