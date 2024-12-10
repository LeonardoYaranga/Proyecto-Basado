from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Sistema de Recomendación de Juegos",
    description="API para recomendar juegos basada en criterios específicos",
    version="1.0.0",
)

app.include_router(router, prefix="/api/v1", tags=["Recomendaciones"])
