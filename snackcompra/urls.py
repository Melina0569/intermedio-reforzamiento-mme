from django.urls import path
from . import views

urlpatterns = [
    path('prefijo/', views.snacks_prefijo, name='snacks_prefijo'),
    path('actualizar-precios/', views.snacks_actualizar_precios, name='snacks_actualizar_precios'),
]