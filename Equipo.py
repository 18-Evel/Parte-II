class Equipo:
    def __init__(self, numero_parte, tipo, descripcion):
        self.numero_parte = numero_parte
        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return f"Equipo {self.tipo} (Parte #{self.numero_parte}): {self.descripcion}"
