class Bus:
    def __init__(self, id, placa):
        self.id = id
        self.placa = placa
        self.ruta = None  
        self.horarios = [] 
        self.conductores_asignados = [] 