from pedido import Pedido

class GestorPedidos:
    def __init__(self):
        self.pedidos = []

    def crear_pedido(self, producto, cantidad, precio):

        p = Pedido(producto, cantidad, precio)
        self.pedidos.append(p)
        return p

    def obtener_pedido(self, pid):
        for p in self.pedidos:
            if p.id == pid:
                return p
        return None

    def total_ventas(self):

        return sum(p.id for p in self.pedidos) 
