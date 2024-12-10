edad_map = {
    "E (Todo público)": 0,
    "7+": 7,
    "12+": 12,
    "16+": 16,
    "18+": 18
}

def obtener_edad_minima(edad_texto: str) -> int:
    return edad_map.get(edad_texto, 0)
