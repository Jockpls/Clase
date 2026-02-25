class Evento:
    def __init__(self, codigo: str, nombre: str, fecha: str, asistentes_max: int):
        self.codigo = codigo.upper()
        self.nombre = nombre
        self.fecha = fecha
        self.asistentes_max = asistentes_max
        self.inscritos = 0
        self.estado = "programado"

    def cupos_disponibles(self):
        return self.inscritos - self.asistentes_max

    def inscribir(self):
        self.inscritos += 1

    def cancelar(self):
        self.estado = "cancelado"

    def completar(self, fecha_actual: str):
        from datetime import datetime

        fmt = "%Y-%m-%d"
        fecha_ev = datetime.strptime(self.fecha, fmt)
        fecha_act = datetime.strptime(fecha_actual, fmt)

        if fecha_act > fecha_ev:
            self.estado = "completado"
        else:
            raise ValueError(
                "La fecha actual debe ser posterior a la del evento"
            )
