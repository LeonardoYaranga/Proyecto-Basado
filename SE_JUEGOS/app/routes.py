import os
from fastapi import APIRouter, HTTPException
from .models import RecomendacionRequest, RecomendacionResponse
from .prolog_helper import PrologHelper
from .services import obtener_edad_minima

router = APIRouter()

# Construir la ruta absoluta y convertir a formato POSIX
current_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta absoluta
prolog_file_path = os.path.join(current_dir, "sistema_experto.pl").replace("\\", "/")  # Convierte barras

prolog_helper = PrologHelper(prolog_file_path)  # Usa la ruta procesada

@router.post("/recomendar/", response_model=RecomendacionResponse)
async def recomendar_juegos(request: RecomendacionRequest):
    anio_actual = 2024  # Año actual (puedes automatizar esto si lo deseas)
    edad_minima = obtener_edad_minima(request.edad)
    
    juegos = prolog_helper.recomendar_juegos(
        plataforma=request.plataforma,
        genero=request.genero,
        jugadores=request.jugadores,
        edad=edad_minima,
        anio_actual=anio_actual
    )
    
    if not juegos:
        raise HTTPException(status_code=404, detail="No se encontraron juegos que cumplan los criterios.")
    
    return RecomendacionResponse(juegos=juegos)
