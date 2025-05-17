class Taller:
    def __init__(self):
        self.clientes = []

    def ingresar_cliente(self, apellidos, nombres, telefono):
        cliente = Cliente(apellidos, nombres, telefono)
        self.clientes.append(cliente)
        print(f"Cliente {nombres} {apellidos} ingresado exitosamente.")

    def ver_clientes(self):
        if self.clientes:
            print("Clientes registrados:")
            for cliente in self.clientes:
                print(f"  - {cliente.nombres} {cliente.apellidos}")
        else:
            print("No hay clientes registrados.")

    def agregar_equipo(self, numero_parte, tipo, descripcion, cliente_nombres):
        cliente = next((c for c in self.clientes if c.nombres == cliente_nombres), None)
        if cliente:
            equipo = Equipo(numero_parte, tipo, descripcion)
            cliente.agregar_equipo(equipo)
            print(f"Equipo {tipo} agregado al cliente {cliente_nombres}.")
        else:
            print(f"Cliente {cliente_nombres} no encontrado.")

    def ver_equipos_por_cliente(self, cliente_nombres):
        cliente = next((c for c in self.clientes if c.nombres == cliente_nombres), None)
        if cliente:
            cliente.mostrar_equipos()
        else:
            print(f"Cliente {cliente_nombres} no encontrado.")
