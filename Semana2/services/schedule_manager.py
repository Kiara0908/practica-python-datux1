def validar_horario(horario):
    try:
        inicio, fin = horario.split("-")
        if "08:00" <= inicio <= "16:00" and "08:00" <= fin <= "16:00" and inicio < fin:
            return True
    except ValueError:
        pass
    return False
