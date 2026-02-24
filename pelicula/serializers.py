from rest_framework import serializers
from .models import Pelicula, SnackCompra



class PeliculaSerializer(serializers.ModelSerializer):
    nombre_director = serializers.SerializerMethodField()
<<<<<<< HEAD
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

=======

    class Meta:
        model = Pelicula
        fields = ['id', 'titulo', 'clasificacion', 'duracion_min', 'genero','nombre_director']

    def get_nombre_director(self, obj):
        # Devuelve un valor ficticio o None si no hay director
        return getattr(obj, 'director', None)  # evita crash
>>>>>>> fa15de0d684b09b0734c34e2a24de3f417f2a78c

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnackCompra
        fields = ['id', 'nombre', 'tipo', 'precio']