class Cliente:
    def __init__(self, apellidos, nombres, telefono):
        self.apellidos = apellidos
        self.nombres = nombres
        self.telefono = telefono
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def mostrar_equipos(self):
        if self.equipos:
            print(f"Equipos de {self.nombres} {self.apellidos}:")
            for equipo in self.equipos:
                print(f"  - {equipo}")
        else:
            print(f"{self.nombres} {self.apellidos} no ha ingresado equipos.")
