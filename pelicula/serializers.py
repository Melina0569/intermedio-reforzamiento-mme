from rest_framework import serializers
from .models import Pelicula, SnackCompra



class PeliculaSerializer(serializers.ModelSerializer):
    nombre_director = serializers.SerializerMethodField()
    total_entradas_vendidas = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pelicula
        fields = [
            'id',
            'titulo',
            'clasificacion',
            'duracion_min',
            'genero',
            'nombre_director',
            'total_entradas_vendidas'
        ]

    def get_nombre_director(self, obj):
        return getattr(obj, 'director', None)


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackCompra
        fields = ['id', 'nombre', 'tipo', 'precio']