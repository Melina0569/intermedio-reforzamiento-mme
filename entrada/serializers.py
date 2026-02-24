from rest_framework import serializers
from .models import Entrada
from funcion.serializers import FuncionSerializer


class EntradaSerializer(serializers.ModelSerializer):

    # Mostrar función de forma anidada
    funcion = FuncionSerializer(read_only=True)

    class Meta:
        model = Entrada
        fields = [
            'id',
            'funcion',
            'asiento',
            'fecha_venta',
            'vendido',
            'precio_final',
        ]