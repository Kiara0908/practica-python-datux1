class Bus:
    def __init__(self, id, placa):
        self.id = id
        self.placa = placa
        self.ruta = None  # Ruta asignada al bus
        self.horarios = []  # Horarios asignados al bus
        self.conductores_asignados = []  # Lista de conductores asignados