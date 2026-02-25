from evento import Evento


class GestorEventos:
    def __init__(self):
        self.eventos = {}

    def crear_evento(self, codigo, nombre, fecha, max_asistentes):
        ev = Evento(codigo, nombre, fecha, max_asistentes)
        self.eventos[codigo] = ev
        return ev

    def obtener_evento(self, codigo):

        return self.eventos.get(codigo, None)

    def inscribir_a_evento(self, codigo):
        ev = self.obtener_evento(codigo)
        if ev is None:
            raise KeyError(f"Evento {codigo} no encontrado")
        ev.inscribir()

    def cancelar_evento(self, codigo):
        ev = self.obtener_evento(codigo)
        if ev is None:
            raise KeyError(f"Evento {codigo} no encontrado")
        ev.cancelar()

    def completar_evento(self, codigo, fecha_actual):
        ev = self.obtener_evento(codigo)
        if ev is None:
            raise KeyError(f"Evento {codigo} no encontrado")
        ev.completar(fecha_actual)

    def total_cupos_libres(self):
        return sum(ev.cupos_disponibles() for ev in self.eventos.values())
