from django.contrib import admin
from .models import Funcion
# Register your models here.

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'estado')  # Columnas visibles
    search_fields = ('estado',)  # Barra de búsqueda
    list_filter = ('estado', 'fecha_hora')  # Filtros laterales
    pass