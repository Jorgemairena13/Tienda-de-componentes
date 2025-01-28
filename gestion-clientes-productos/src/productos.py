class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar_producto(self, productos):
        productos.append(self)

    def eliminar_producto(self, productos):
        productos.remove(self)

    @staticmethod
    def listar_productos(productos):
        return [vars(producto) for producto in productos]