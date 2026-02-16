from django.urls import path
from . import views

urlpatterns = [
    path("orden-mixto/",views.funciones_orden_mixto_view,name="funciones_orden_mixto"),
]