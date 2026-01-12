from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Animal(ABC):

    @abstractmethod
    def hablar():
        pass

class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre}, dice Guau"

class Gato(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre}, dice miau"

class Caballo(Animal):

    def __init__(self, nombre = "Horse Luis"):
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre}, dice: voy!"

class Vaca(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre} pregunta si puede bajar Horse Luis"


def main():
    firulais = Perro("firulais")
    print(firulais.hablar())
    misifu = Gato("Misifú")
    print(misifu.hablar())
    vacaquerie = Vaca("LaVacaQueRie")
    print(vacaquerie.hablar())
    horseluis = Caballo()
    print(horseluis.hablar())
main()