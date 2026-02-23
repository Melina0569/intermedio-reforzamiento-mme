from rest_framework import serializers
from .models import Pelicula, SnackCompra



class PeliculaSerializer(serializers.ModelSerializer):
    nombre_director = serializers.SerializerMethodField()

    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'clasificacion', 'duracion_min', 'genero','nombre_director']

    def get_nombre_director(self, obj):
        # Devuelve un valor ficticio o None si no hay director
        return getattr(obj, 'director', None)  # evita crash

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackCompra
        fields = ['id', 'nombre', 'tipo', 'precio']