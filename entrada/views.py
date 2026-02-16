from django.shortcuts import render
from .models import Entrada

def entradas_rango(request):
    entradas = Entrada.objects.all()[4:7]  # índices 4,5,6
    return render(request, 'cine/entradas_rango.html', {'entradas': entradas})


def entrada_eliminar(request, id):
    context = {}
    try:
        # Intentar obtener la entrada por ID
        entrada = Entrada.objects.get(id=id)
        codigo_eliminado = entrada.codigo  # guardar el código antes de eliminar
        entrada.delete()  # eliminar la entrada
        context['mensaje'] = f"Entrada eliminada: {codigo_eliminado}"
    except Entrada.DoesNotExist:
        # Si no existe la entrada
        context['mensaje'] = "No existe esa entrada en la base de datos"

    return render(request, 'cine/entrada_eliminar.html', context)
