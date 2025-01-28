class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"Cliente(nombre={self.nombre}, email={self.email})"


class GestionClientes:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def eliminar_cliente(self, email):
        self.clientes = [cliente for cliente in self.clientes if cliente.email != email]

    def listar_clientes(self):
        return self.clientes