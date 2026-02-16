from django.urls import path
from . import views

urlpatterns = [
    path('rango/', views.entradas_rango, name='entradas_rango'),
    path('entradas/<int:id>/eliminar/', views.entrada_eliminar, name='entrada_eliminar'),
]