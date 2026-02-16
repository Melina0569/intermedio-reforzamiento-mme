from django.shortcuts import render
from django.db.models import F
from .models import SnackCompra

def snacks_prefijo(request):
    prefijo = request.GET.get('texto', '')
    if prefijo:
        snacks = SnackCompra.objects.filter(producto__istartswith=prefijo)
    else:
        snacks = SnackCompra.objects.all()
    return render(request, 'cine/snacks_prefijo.html', {'snacks': snacks, 'prefijo': prefijo})

def snacks_actualizar_precios(request):
    # 1️⃣ Definir variables
    min_precio = 10      # precio mínimo para filtrar
    descuento = 2        # monto a restar al precio_unitario

    # 2️⃣ Filtrar snacks que cumplen la condición
    snacks_filtrados = SnackCompra.objects.filter(precio_unitario__gte=min_precio)

    # 3️⃣ Actualizar precios usando F expressions
    snacks_filtrados.update(precio_unitario=F('precio_unitario') - descuento)

    # 4️⃣ Volver a consultar los snacks actualizados para mostrar
    snacks_actualizados = SnackCompra.objects.filter(precio_unitario__gte=(min_precio - descuento))

    # 5️⃣ Enviar al template
    context = {
        'snacks': snacks_actualizados,
        'min_precio': min_precio,
        'descuento': descuento
    }
    return render(request, 'cine/snacks_actualizar_precios.html', context)
