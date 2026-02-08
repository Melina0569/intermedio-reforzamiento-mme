from django.shortcuts import render

def peliculas_list_view(request):
    data_context = [
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
        },
        {
            "id": 3,
            "titulo": "Toy Story",
            "duracion_min": 81,
            "genero": "Animación",
            "clasificacion": "G"
        },
    ]

    return render(request, 'cine/peliculas_list.html', context={'data': data_context})

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




