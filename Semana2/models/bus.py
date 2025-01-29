class Bus:
    def __init__(self, id, placa):
        self.id = id
        self.placa = placa
        self.ruta = None  # Ruta asignada al bus
        self.horarios = []  # Horarios asignados al bus (ej. ["09:00-11:00"])
        self.conductores_asignados = []  # Lista de conductores asignados
