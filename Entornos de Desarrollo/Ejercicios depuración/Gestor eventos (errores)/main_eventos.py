from gestor_eventos import GestorEventos

def main():
    g = GestorEventos()

    # Creación de eventos
    g.crear_evento("ev001", "Charla IA", "2024-06-15", 30)
    g.crear_evento("ev002", "Taller Python", "2024-07-01", 20)

    # Inscripciones
    for _ in range(5):
        g.inscribir_a_evento("ev001")
    for _ in range(3):
        g.inscribir_a_evento("ev002")

    # Cancelar un evento
    g.cancelar_evento("ev002")

    # Completar un evento (simulamos fecha actual)
    g.completar_evento("ev001", "2024-06-16")

    # Mostrar información
    print(f"Cupos libres totales: {g.total_cupos_libres()}")
    ev1 = g.obtener_evento("ev001")
    ev2 = g.obtener_evento("ev002")
    print(f"Estado EV001: {ev1.estado}, inscritos: {ev1.inscritos}")
    print(f"Estado EV002: {ev2.estado}, inscritos: {ev2.inscritos}")

if __name__ == "__main__":
    main()
