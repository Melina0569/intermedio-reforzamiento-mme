from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'genero', 'clasificacion', 'duracion_min']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion_min': forms.NumberInput(attrs={'class': 'form-control'}),
        }