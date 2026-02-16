from django.shortcuts import render
from .models import Funcion

def funciones_orden_mixto_view(request):
    funciones = Funcion.objects.order_by("estado", "-fecha_hora")

    return render(
        request,
        "cine/funciones_orden_mixto.html",
        {"funciones": funciones}
    )
