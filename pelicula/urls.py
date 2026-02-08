from django.urls import path
from . import views

urlpatterns = [
    path('peliculas/', views.peliculas_list_view, name='peliculas_list'),
    path("peliculas/<int:id>/", views.pelicula_detail_view, name="pelicula_detail"),
    path("peliculas/<int:id>/funciones/", views.funciones_list_view, name="funciones_list"),
    path("funciones/<int:id>/entradas/", views.entradas_list_view, name="entradas_list"),
    path("entradas/<int:id>/snacks/", views.snacks_list_view, name="snacks_list"),
    path("cartelera/", views.cartelera_view, name="cartelera"),
    path("", views.home_view, name="home"),
]