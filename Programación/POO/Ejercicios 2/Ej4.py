from abc import ABC, abstractmethod
from beartype import beartype

@beartype
class Electrodomestico(ABC):
    #No necesito un constructor
    @property
    @abstractmethod
    def consumo():
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

    @property
    @abstractmethod
    def modelo(self):
        pass

class Lavadora(Electrodomestico):

    @property
    def consumo(self) -> float:
        return 21.4

    @property
    def marca(self):
        return 'Electrolux'

    @property
    def modelo(self):
        return 'El que gira'

    def __str__(self):
        return f"La marca de la lavadora es {self.marca}, con el modelo {self.modelo} y consume {self.consumo}kw"

class Televisor(Electrodomestico):

    @property
    def consumo(self) -> float:
        return 15.6

    @property
    def marca(self):
        return 'Samsung'

    @property
    def modelo(self):
        return 'Otro'

    def __str__(self):
        return f"La marca del televisor es {self.marca}, con el modelo {self.modelo} y consume {self.consumo}kw"

class Microondas(Electrodomestico):

    @property
    def consumo(self) -> float:
        return 5.2

    @property
    def marca(self):
        return 'LG'

    @property
    def modelo(self):
        return 'WebOs'

    def __str__(self):
        return f"La marca del microondas es {self.marca}, con el modelo {self.modelo} y consume {self.consumo}kw"
def main():
    lava = Lavadora()
    tele = Televisor()
    micro = Microondas()
    print(lava.__str__())
    print(tele.__str__())
    print(micro.__str__())
main()
