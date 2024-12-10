from pyswip import Prolog

class PrologHelper:
    def __init__(self, file_path: str):
        self.prolog = Prolog()
        self.prolog.consult(file_path)
    
    def recomendar_juegos(self, plataforma: str, genero: str, jugadores: int, edad: int, anio_actual: int):
        query = f"recomendar_juego(Juego, '{plataforma}', '{genero}', {jugadores}, {edad}, {anio_actual})"
        resultados = list(self.prolog.query(query))
        return [res["Juego"] for res in resultados]
