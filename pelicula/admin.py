from django.contrib import admin
from .models import Pelicula
# Register your models here.

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'clasificacion') #Columnas visibles
    search_fields = ('titulo', 'genero') #Barra de busqueda
    list_filter = ('genero', 'clasificacion') #Filtros laterales
    pass