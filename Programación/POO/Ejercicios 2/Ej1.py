from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Figura(ABC):

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Rectangulo(Figura):
    def __init__(self, lado: float, ancho: float):
        self.lado = lado
        self.ancho = ancho

    def perimetro(self)-> float:
        return (self.lado*2) + (self.ancho+2)
    def area(self)-> float:
        return self.lado * self.ancho

class Cuadrado(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def perimetro(self)-> float:
        return self.lado*4

    def area(self)-> float:
        return self.lado**2

def main():
    cuadradito = Cuadrado(6)
    print(f"El area de Cuadradito es {cuadradito.area()}")
    print(f"El perímetro de Cuadradito es {cuadradito.perimetro()}")
    rectangulito = Rectangulo(2, 4)
    print(f"El area de Rectangulito es {rectangulito.area()}")
    print(f"El perimetro de Rectangulito es {rectangulito.perimetro()}")


main()