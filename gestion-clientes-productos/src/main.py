# Contenido del archivo /gestion-clientes-productos/gestion-clientes-productos/src/main.py

from clientes import Cliente
from productos import Producto
from utils.json_handler import cargar_datos, guardar_datos

def main():
    clientes = cargar_datos('data/clientes.json')
    productos = cargar_datos('data/productos.json')

    while True:
        print("1. Agregar Cliente")
        print("2. Eliminar Cliente")
        print("3. Listar Clientes")
        print("4. Agregar Producto")
        print("5. Eliminar Producto")
        print("6. Listar Productos")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Introduce el nombre del cliente: ")
            cliente = Cliente(nombre)
            clientes.append(cliente)
            guardar_datos('data/clientes.json', clientes)
        elif opcion == '2':
            nombre = input("Introduce el nombre del cliente a eliminar: ")
            clientes = [c for c in clientes if c.nombre != nombre]
            guardar_datos('data/clientes.json', clientes)
        elif opcion == '3':
            for cliente in clientes:
                print(cliente.nombre)
        elif opcion == '4':
            nombre = input("Introduce el nombre del producto: ")
            producto = Producto(nombre)
            productos.append(producto)
            guardar_datos('data/productos.json', productos)
        elif opcion == '5':
            nombre = input("Introduce el nombre del producto a eliminar: ")
            productos = [p for p in productos if p.nombre != nombre]
            guardar_datos('data/productos.json', productos)
        elif opcion == '6':
            for producto in productos:
                print(producto.nombre)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()