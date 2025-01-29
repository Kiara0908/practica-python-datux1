from models.bus import Bus
from models.conductor import Conductor

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, id, placa):
        nuevo_bus = Bus(id, placa)
        self.buses.append(nuevo_bus)
        print(f"Bus con ID {id} y placa {placa} agregado correctamente.")

    def agregar_ruta_a_bus(self, id_bus, ruta):
        bus = self.buscar_bus(id_bus)
        if bus:
            bus.ruta = ruta
            print(f"Ruta '{ruta}' asignada al bus con ID {id_bus}.")
        else:
            print("Bus no encontrado.")

    def registrar_horario_a_bus(self, id_bus, horario):
        if not self.validar_horario(horario):
            print("Horario inválido. Debe estar entre 08:00 y 16:00.")
            return

        bus = self.buscar_bus(id_bus)
        if bus:
            if horario not in bus.horarios:
                bus.horarios.append(horario)
                print(f"Horario '{horario}' registrado para el bus con ID {id_bus}.")
            else:
                print("El horario ya está registrado para este bus.")
        else:
            print("Bus no encontrado.")

    def agregar_conductor(self, id, nombre):
        nuevo_conductor = Conductor(id, nombre)
        self.conductores.append(nuevo_conductor)
        print(f"Conductor con ID {id} y nombre {nombre} agregado correctamente.")

    def agregar_horario_a_conductor(self, id_conductor, horario):
        if not self.validar_horario(horario):
            print("Horario inválido. Debe estar entre 08:00 y 16:00.")
            return

        conductor = self.buscar_conductor(id_conductor)
        if conductor:
            if horario not in conductor.horarios:
                conductor.horarios.append(horario)
                print(f"Horario '{horario}' agregado al conductor con ID {id_conductor}.")
            else:
                print("El horario ya está registrado para este conductor.")
        else:
            print("Conductor no encontrado.")

    def asignar_bus_a_conductor(self, id_bus, id_conductor, horario):
        if not self.validar_horario(horario):
            print("Horario inválido. Debe estar entre 08:00 y 16:00.")
            return

        bus = self.buscar_bus(id_bus)
        conductor = self.buscar_conductor(id_conductor)

        if bus and conductor:
            if horario in bus.horarios:
                for c in bus.conductores_asignados:
                    if horario in c.horarios:
                        print("Este horario ya está asignado a otro conductor en este bus.")
                        return

                if horario in conductor.horarios:
                    bus.conductores_asignados.append(conductor)
                    print(f"Conductor {id_conductor} asignado al bus {id_bus} para el horario {horario}.")
                else:
                    print("El conductor no tiene este horario registrado.")
            else:
                print("El horario no está registrado para este bus.")
        else:
            print("Bus o conductor no encontrado.")

    def buscar_bus(self, id_bus):
        for bus in self.buses:
            if bus.id == id_bus:
                return bus
        return None

    def buscar_conductor(self, id_conductor):
        for conductor in self.conductores:
            if conductor.id == id_conductor:
                return conductor
        return None

    def validar_horario(self, horario):
        try:
            inicio, fin = horario.split("-")
            if "08:00" <= inicio <= "16:00" and "08:00" <= fin <= "16:00" and inicio < fin:
                return True
        except ValueError:
            pass
        return False