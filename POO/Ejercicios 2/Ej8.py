from abc import ABC, abstractmethod
from beartype import beartype
from random import randint

@beartype
class Juego(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class JuegoAdivinarNumero(Juego):
    def __init__(self):
        self.__numero = randint(1, 10)

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    def ejecutar(self):
        while True:
            intento = int(input(f'Dame un número entre 1 y 10, a ver si adivinas el mío. '))
            if intento < self.__numero:
                print('Inténtalo de nuevo, es más alto. ')
            elif intento > self.__numero:
                print('Intentalo de nuevo es más bajo. ')
            else:
                print("Tenías que saberlo.")
                break

    def __str__(self):
        return f'El número es {self.numero}'

def main():
    juego = JuegoAdivinarNumero()
    juego.ejecutar()
    print(juego)
if __name__ == '__main__':
    main()

