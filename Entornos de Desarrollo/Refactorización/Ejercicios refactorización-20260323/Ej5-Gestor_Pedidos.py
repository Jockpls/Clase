"""
GestorPedidos refactorizado - Versión Python

Mejoras aplicadas:
  - Eliminadas variables booleanas intermedias innecesarias
  - Ramas muertas en if/else reemplazadas por expresiones directas
  - Switch con ramas duplicadas simplificado
  - Condiciones negadas doblemente eliminadas
  - is_pedido_entregado_a_tiempo() reducido a expresión booleana directa
  - Comparaciones explícitas a true/false eliminadas
  - get_estado_descripcion() convertido a match/case
  - calcular_precio_final() extraído en métodos privados cohesivos
"""


class GestorPedidos:
    """Clase para gestionar pedidos"""
    
    def __init__(self, cliente_nombre: str, cliente_tipo: str,
                 total_pedido: float, cantidad_articulos: int,
                 cliente_verificado: bool, pedido_urgente: bool,
                 metodo_pago: str, estado_pedido: str,
                 dias_entrega: int):
        self.cliente_nombre = cliente_nombre
        self.cliente_tipo = cliente_tipo
        self.total_pedido = total_pedido
        self.cantidad_articulos = cantidad_articulos
        self.cliente_verificado = cliente_verificado
        self.pedido_urgente = pedido_urgente
        self.metodo_pago = metodo_pago
        self.estado_pedido = estado_pedido
        self.dias_entrega = dias_entrega
    
    def is_pedido_activo(self) -> bool:
        return self.estado_pedido != "CANCELADO"
    
    def is_cliente_elegible_descuento(self) -> bool:
        return self.total_pedido > 100
    
    def is_pedido_listo_para_enviar(self) -> bool:
        return self.cliente_verificado and self.estado_pedido != "CANCELADO"
    
    def calcular_precio_final(self) -> float:
        return (self.total_pedido 
                - self._calcular_descuento() 
                + self._calcular_recargo_pago() 
                + self._calcular_recargo_urgente())
    
    def is_pedido_entregado_a_tiempo(self) -> bool:
        if self.pedido_urgente:
            return self.dias_entrega <= 1
        return self.dias_entrega <= 3
    
    def is_pedido_prioritario(self) -> bool:
        return self.pedido_urgente and self.cliente_verificado
    
    def get_estado_descripcion(self) -> str:
        match self.estado_pedido:
            case "PENDIENTE":
                return "El pedido está pendiente de procesar"
            case "PROCESANDO":
                return "El pedido se está procesando"
            case "ENVIADO":
                return "El pedido ha sido enviado"
            case "CANCELADO":
                return "El pedido ha sido cancelado"
            case _:
                return "Estado desconocido"
    
    # Métodos privados extraídos de calcular_precio_final()
    
    def _calcular_descuento(self) -> float:
        match self.cliente_tipo:
            case "VIP":
                return self.total_pedido * 0.15
            case "EMPLEADO":
                return self.total_pedido * 0.25
            case _:
                return 0
    
    def _calcular_recargo_pago(self) -> float:
        if self.metodo_pago == "TARJETA":
            return self.total_pedido * 0.02
        return 0
    
    def _calcular_recargo_urgente(self) -> float:
        return 15.0 if self.pedido_urgente else 0
