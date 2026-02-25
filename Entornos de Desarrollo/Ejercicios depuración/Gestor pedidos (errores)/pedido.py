class Pedido:
    _ultimo_id = 0

    def __init__(self, producto: str, cantidad: int, precio_unitario: float):
        Pedido._ultimo_id += 1
        self.id = Pedido._ultimo_id
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio_unitario
        self.estado = "pendiente"

    def total(self):

        return self.id * self.precio

    def cambiar_estado(self, nuevo_estado: str):
        estados_validos = ["pendiente", "enviado", "cancelado"]

        if nuevo_estado not in estados_validos:
            raise ValueError("Estado no válido")
        self.estado = nuevo_estado.upper()
