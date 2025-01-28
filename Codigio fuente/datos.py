import json
from os import path

# Funciones para cargar datos
def cargar_datos():
    # Inicializamos los diccionarios vacíos por defecto
    datos = {
        "clientes": {},
        "articulos": {
            "id_1": {"nombre": "Procesador", "precio": 100, "Stock": 50},
            # ... resto de productos predeterminados
        },
        "ventas": {},
    }
    
    # Intentamos cargar el archivo si existe
    try:
        if path.exists('datos_tienda.json'):
            with open('datos_tienda.json', 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
    except Exception as e:
        print(f"Error al cargar datos: {e}")
    
    return datos["clientes"], datos["articulos"], datos["ventas"]

# Función para guardar datos
def guardar_datos(clientes, articulos, ventas):
    datos = {
        "clientes": clientes,
        "articulos": articulos,
        "ventas": ventas
    }
    
    try:
        with open('datos_tienda.json', 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar datos: {e}")