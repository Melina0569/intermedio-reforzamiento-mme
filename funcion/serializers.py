from rest_framework import serializers
from .models import Funcion


class FuncionSerializer(serializers.ModelSerializer):

    # Mostrar el título de la película
    pelicula_titulo = serializers.CharField(
        source='pelicula.titulo',
        read_only=True
    )

    class Meta:
        model = Funcion
        fields = [
            'id',
            'pelicula',
            'pelicula_titulo',
            'estado',
            'fecha_hora',
            'precio',
        ]