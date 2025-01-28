# Proyecto de Gestión de Clientes y Productos

Este proyecto permite gestionar clientes y productos utilizando archivos en formato JSON para el almacenamiento de datos.

## Estructura del Proyecto

```
gestion-clientes-productos
├── src
│   ├── clientes.py        # Clase Cliente para gestionar clientes
│   ├── productos.py       # Clase Producto para gestionar productos
│   ├── main.py            # Punto de entrada de la aplicación
│   └── utils
│       └── json_handler.py # Funciones para manejar archivos JSON
├── data
│   ├── clientes.json      # Almacena información de clientes
│   └── productos.json     # Almacena información de productos
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación del proyecto
```

## Instalación

1. Clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/main.py
```

Sigue las instrucciones en pantalla para gestionar clientes y productos.