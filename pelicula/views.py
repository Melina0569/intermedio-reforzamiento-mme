from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pelicula, Funcion, SnackCompra
from .forms import PeliculaForm
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import PeliculaSerializer, SnackSerializer
from django_filters.rest_framework import DjangoFilterBackend
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q, F
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


=======
>>>>>>> fa15de0d684b09b0734c34e2a24de3f417f2a78c
def pelicula_unica_view(request):

    titulo = request.GET.get('titulo')
    clasificacion = request.GET.get('clasificacion')

    pelicula = None

    if titulo and clasificacion:
        try:
            pelicula = Pelicula.objects.get(
                titulo=titulo,
                clasificacion=clasificacion
            )
        except Pelicula.DoesNotExist:
            pelicula = None

    return render(request, 'cine/pelicula_unica.html', {'pelicula': pelicula})

def peliculas_contiene_view(request):
    texto = request.GET.get('q', '')

    peliculas = Pelicula.objects.filter(titulo__icontains=texto) if texto else []

    context = {
        'peliculas': peliculas,
        'texto': texto
    }

    return render(request, 'cine/peliculas_contiene.html', context)

def peliculas_termina_view(request):

    texto = request.GET.get('q', '')

    if texto:
        peliculas = Pelicula.objects.filter(titulo__iendswith=texto)
    else:
        peliculas = []

    context = {
        'peliculas': peliculas,
        'texto': texto
    }

    return render(request, 'cine/peliculas_termina.html', context)

def funciones_orden_mixto_view(request):

    funciones = Funcion.objects.order_by('estado', '-fecha_hora')

    context = {
        'funciones': funciones
    }

    return render(request, 'cine/funciones_orden_mixto.html', context)

def peliculas_actualizar(request):
    # 1️⃣ Obtener parámetros del GET
    pref = request.GET.get('pref', '')  # prefijo del género o título
    nueva_clasificacion = request.GET.get('nueva_clasificacion', '')  # nueva clasificación

    # 2️⃣ Actualización masiva usando ORM
    if pref and nueva_clasificacion:
        Pelicula.objects.filter(genero__startswith=pref).update(clasificacion=nueva_clasificacion)

    # 3️⃣ Consultar las películas que coinciden con el prefijo después de actualizar
    peliculas = Pelicula.objects.filter(genero__startswith=pref).order_by("titulo")

    # 4️⃣ Enviar al template
    context = {
        'peliculas': peliculas,
        'pref': pref,
        'nueva_clasificacion': nueva_clasificacion
    }
    return render(request, 'cine/peliculas_actualizar.html', context)

def pelicula_detail_view(request, id):
    pelicula_encontrada = None

    peliculas = [
        {
            "id": 1,
            "titulo": "Avengers",
            "duracion_min": 143,
            "genero": "Acción",
            "clasificacion": "PG-13"
        },
        {
            "id": 2,
            "titulo": "Titanic",
            "duracion_min": 195,
            "genero": "Drama",
            "clasificacion": "PG-13"
        }
    ]
    for pelicula in peliculas:
        if pelicula["id"] == id:
            pelicula_encontrada = pelicula
            break

    return render(request,'cine/pelicula_detail.html',context={'pelicula': pelicula_encontrada})


from django.shortcuts import render

def funciones_list_view(request, id):
    # Películas hardcodeadas (solo para obtener el título)
    peliculas = [
        {"id": 1, "titulo": "Avengers"},
        {"id": 2, "titulo": "Titanic"},
        {"id": 3, "titulo": "Toy Story"},
    ]

    pelicula = None
    for p in peliculas:
        if p["id"] == id:
            pelicula = p
            break

    # Funciones hardcodeadas
    funciones = [
        {"hora": "14:00", "precio": 15, "estado": "Disponible"},
        {"hora": "17:30", "precio": 18, "estado": "Disponible"},
        {"hora": "21:00", "precio": 20, "estado": "Agotado"},
    ]

    return render(request,"cine/funciones_list.html",context={"pelicula": pelicula,"funciones": funciones}
    )

def entradas_list_view(request, id):
    # Entradas hardcodeadas
    entradas = [
        {
            "codigo": "E001",
            "asiento": "A1",
            "estado": "Vendido",
            "fecha_venta": "2025-02-01"
        },
        {
            "codigo": "E002",
            "asiento": "A2",
            "estado": "Vendido",
            "fecha_venta": "2025-02-01"
        },
        {
            "codigo": "E003",
            "asiento": "B1",
            "estado": "Disponible",
            "fecha_venta": "-"
        }
    ]
    return render(request,"cine/entradas_list.html",context={"entradas": entradas})

def snacks_list_view(request, id):
    # Snacks hardcodeados
    snacks = [
        {"entrada_id": 1, "producto": "Popcorn", "cantidad": 2, "precio_unitario": 8},
        {"entrada_id": 1, "producto": "Gaseosa", "cantidad": 1, "precio_unitario": 5},
        {"entrada_id": 2, "producto": "Nachos", "cantidad": 1, "precio_unitario": 10},
        {"entrada_id": 2, "producto": "Gaseosa", "cantidad": 2, "precio_unitario": 5},
    ]

    # Filtrar snacks por entrada_id
    snacks_filtrados = []
    total_snacks = 0

    for snack in snacks:
        if snack["entrada_id"] == id:
            snacks_filtrados.append(snack)
            total_snacks += snack["cantidad"] * snack["precio_unitario"]

    return render(request,"cine/snacks_list.html",context={"entrada_id": id,"snacks": snacks_filtrados,"total_snacks": total_snacks})

def cartelera_view(request):
    # Películas hardcodeadas (activas y no activas)
    peliculas = [
        {"id": 1, "titulo": "Avengers", "activa": True},
        {"id": 2, "titulo": "Titanic", "activa": False},
        {"id": 3, "titulo": "Toy Story", "activa": True},
        {"id": 4, "titulo": "Avatar", "activa": True},
    ]

    # Filtrar solo películas activas
    peliculas_activas = []
    for pelicula in peliculas:
        if pelicula["activa"]:
            peliculas_activas.append(pelicula)

    return render(request,"cine/cartelera.html",context={"peliculas": peliculas_activas})

def home_view(request):
    return render(request,"cine/home.html",context={"nombre_cine": "Cine San Marcos","pelicula_destacada": "Avengers","total_funciones": 12})


class PeliculaList(ListView):
    model = Pelicula
    template_name = 'cine/peliculas_list.html'
    context_object_name = 'peliculas'
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]


class PeliculaCreate(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'cine/pelicula_form.html'
    success_url = reverse_lazy('peliculas_list')
    permission_classes = [IsAuthenticated]

class PeliculaUpdate(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'cine/pelicula_form.html'
    success_url = reverse_lazy('peliculas_list')
    permission_classes = [IsAuthenticated]

class PeliculaDelete(DeleteView):
    model = Pelicula
    template_name = 'cine/pelicula_confirm_delete.html'
    success_url = reverse_lazy('peliculas_list')
    permission_classes = [IsAuthenticated]

class PeliculaSearchAPI(generics.ListAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'genero', 'clasificacion']
    permission_classes = [IsAuthenticated]

class SnackListAPIView(generics.ListAPIView):
    queryset = SnackCompra.objects.all()
    serializer_class = SnackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'tipo']  # campos por los que se puede filtrar
    permission_classes = [IsAuthenticated]

class PeliculasTopVendidasAPIView(generics.ListAPIView):
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Pelicula.objects
            .annotate(
                total_entradas_vendidas=Count(
                    'funcion__entrada',
                    filter=Q(funcion__entrada__vendido=True)
                )
            )
            .filter(total_entradas_vendidas__gte=1)
            .order_by('-total_entradas_vendidas')
        )

class PeliculaCreateAPIView(generics.CreateAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]

class PeliculaDeleteAPIView(generics.DestroyAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

class ActualizarPreciosSnacksAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        min_precio = request.data.get("min_precio")
        descuento = request.data.get("descuento")

        # Validar datos obligatorios
        if min_precio is None or descuento is None:
            return Response(
                {"error": "Debe enviar min_precio y descuento"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Obtener snacks que cumplen condición
        snacks = SnackCompra.objects.filter(precio__gte=min_precio)

        # Validar que descuento no sea mayor al precio
        for snack in snacks:
            if descuento > snack.precio:
                return Response(
                    {"error": f"El descuento no puede ser mayor al precio del snack {snack.nombre}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Actualización masiva con F expression
        snacks.update(precio= F('precio') - descuento)

        # Refrescar queryset actualizado
        snacks_actualizados = SnackCompra.objects.filter(precio__gte=0)

        serializer = SnackSerializer(snacks_actualizados, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

=======
>>>>>>> fa15de0d684b09b0734c34e2a24de3f417f2a78c


class PeliculaCreate(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'cine/pelicula_form.html'
    success_url = reverse_lazy('peliculas_list')

class PeliculaUpdate(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'cine/pelicula_form.html'
    success_url = reverse_lazy('peliculas_list')

class PeliculaDelete(DeleteView):
    model = Pelicula
    template_name = 'cine/pelicula_confirm_delete.html'
    success_url = reverse_lazy('peliculas_list')

class PeliculaSearchAPI(generics.ListAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'genero', 'clasificacion']

class SnackListAPIView(generics.ListAPIView):
    queryset = SnackCompra.objects.all()
    serializer_class = SnackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'tipo']  # campos por los que se puede filtrar
