class CocheSeguro:
    def __init__(self, tipo: str, antiguedad: int):
        self.tipo = tipo.title()
        self.antiguedad = antiguedad

    def recargo_antiguedad(self):

        if self.antiguedad <= 2:
            return 0.15
        elif 3 <= self.antiguedad <= 5:
            return 0.0
        else:
            return 0.05
