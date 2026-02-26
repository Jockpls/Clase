from gestor import GestorPedidos

def main():
    g = GestorPedidos()
    p1 = g.crear_pedido("Camisa", 2, 25.0)
    p2 = g.crear_pedido("Zapatos", 1, 80.0)

    p1.cambiar_estado("enviado")
    p2.cambiar_estado("cancelado")

    print(f"Total ventas: {g.total_ventas():.2f} €")

if __name__ == "__main__":
    main() 
