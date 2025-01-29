from models.admin import Admin

def menu():
    admin = Admin()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar bus")
        print("2. Agregar ruta a bus")
        print("3. Registrar horario a bus")
        print("4. Agregar conductor")
        print("5. Agregar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del bus: ")
            placa = input("Ingrese placa del bus: ")
            admin.agregar_bus(id, placa)

        elif opcion == "2":
            id_bus = input("Ingrese ID del bus: ")
            ruta = input("Ingrese la ruta del bus: ")
            admin.agregar_ruta_a_bus(id_bus, ruta)

        elif opcion == "3":
            id_bus = input("Ingrese ID del bus: ")
            horario = input("Ingrese el horario: ")
            admin.registrar_horario_a_bus(id_bus, horario)

        elif opcion == "4":
            id = input("Ingrese ID del conductor: ")
            nombre = input("Ingrese nombre del conductor: ")
            admin.agregar_conductor(id, nombre)

        elif opcion == "5":
            id_conductor = input("Ingrese ID del conductor: ")
            horario = input("Ingrese el horario: ")
            admin.agregar_horario_a_conductor(id_conductor, horario)

        elif opcion == "6":
            id_bus = input("Ingrese ID del bus: ")
            id_conductor = input("Ingrese ID del conductor: ")
            horario = input("Ingrese el horario: ")
            admin.asignar_bus_a_conductor(id_bus, id_conductor, horario)

        elif opcion == "7":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
