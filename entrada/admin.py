from django.contrib import admin
from .models import Entrada

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('get_funcion', 'codigo', 'asiento', 'vendido', 'fecha_venta')

    # metodo para mostrar la función relacionada
    def get_funcion(self, obj):
        return obj.funcion.nombre  # o el campo que quieras mostrar del modelo Funcion

    get_funcion.short_description = 'Función'