from django.urls import path
from . import views
from .views import PeliculaList, PeliculaCreate, PeliculaUpdate, PeliculaDelete, PeliculaSearchAPI

urlpatterns = [
    path('peliculas/', PeliculaList.as_view(), name='peliculas_list'),
    path("peliculas/<int:id>/", views.pelicula_detail_view, name="pelicula_detail"),
    path("peliculas/<int:id>/funciones/", views.funciones_list_view, name="funciones_list"),
    path("funciones/<int:id>/entradas/", views.entradas_list_view, name="entradas_list"),
    path("entradas/<int:id>/snacks/", views.snacks_list_view, name="snacks_list"),
    path("cartelera/", views.cartelera_view, name="cartelera"),
    path("", views.home_view, name="home"),
    path('peliculas/nueva/', PeliculaCreate.as_view(), name='pelicula_create'),
    path('peliculas/unica/', views.pelicula_unica_view, name='pelicula_unica'),
    path('peliculas/contiene/', views.peliculas_contiene_view, name='peliculas_contiene'),
    path('peliculas/termina/', views.peliculas_termina_view, name='peliculas_termina'),
    path('funciones/orden-mixto/', views.funciones_orden_mixto_view, name='funciones_orden_mixto'),
    path('actualizar/', views.peliculas_actualizar, name='peliculas_actualizar'),
    path('editar/<int:pk>/', PeliculaUpdate.as_view(), name='pelicula_update'),
    path('eliminar/<int:pk>/', PeliculaDelete.as_view(), name='pelicula_delete'),
    path('api/buscar/', PeliculaSearchAPI.as_view(), name='api_peliculas_buscar'),
    path('eliminar/<int:pk>/', PeliculaDelete.as_view(), name='pelicula_delete'),
    path('api/snacks/', views.SnackListAPIView.as_view(), name='api_snacks'),

]