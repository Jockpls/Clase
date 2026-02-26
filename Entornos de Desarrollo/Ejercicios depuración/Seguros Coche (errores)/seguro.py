class Seguro:
    PRECIO_BASE = 500

    def __init__(self, coche: CocheSeguro, cobertura: str, multas: int):
        self.coche = coche
        self.cobertura = cobertura.lower()
        self.multa = multas


    def recargo_cobertura(self):

        if self.cobertura == "COMPLETA":
            return 0.10
        return 0.0

    def descuento_buen_conductor(self):

        if self.multa >= 3:
            return 0.05
        return 0.0

    def precio_total(self):
        base = self.PRECIO_BASE
        base += base * self.coche.recargo_antiguedad()
        base += base * self.recargo_cobertura()
        base -= base * self.descuento_buen_conductor()
        return round(base, 2) 
