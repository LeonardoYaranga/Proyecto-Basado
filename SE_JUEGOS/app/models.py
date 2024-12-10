from pydantic import BaseModel

class RecomendacionRequest(BaseModel):
    plataforma: str
    genero: str
    jugadores: int
    edad: str

class RecomendacionResponse(BaseModel):
    juegos: list[str]
