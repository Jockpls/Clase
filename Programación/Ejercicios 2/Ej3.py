from abc import ABC, abstractmethod     #Importamos metodo abstracto y clase abstracta
from beartype import beartype           #Importamos el typechecked

@beartype
class Vehículo(ABC):

    #No necesitamos un constructor en una clase abstracta
    @property
    @abstractmethod                       #Pero si quiero definir una propiedad en todas las clases hijas, creo un property para definirlo
    def ruedas(self):       #No necesito un setter para una propiedad que ya defino en el metodo
        pass

    @abstractmethod         #Metodo para arrancar, espero un true o un false
    def arrancar(self):
        pass

    @abstractmethod         #Metodo para detener, espero un true o un false
    def detener(self):
        pass

    @abstractmethod         #Metodo para saber los detalles y si está encendida o apagada
    def info(self):
        pass

    @abstractmethod         #Veamos el estado de la clase en cualquier momento
    def __repr__(self):
        pass

class Moto(Vehículo):
    def __init__(self, marca: str, modelo: str):    #Constructor de moto
        self.marca = marca
        self.modelo = modelo
        self.funciona = False
    @property
    def ruedas(self):                           #No necesito almacenar en memoria la cantidad de ruedas que tiene una moto
        return 2

                       #Si la moto está apagada, la arranco
    def arrancar(self):
        if self.funciona == False:
            self.funciona = True
            return self.funciona



    def detener(self):                           #Si la moto funciona, la paro
        if self.funciona == True:
            self.funciona = False
            return self.funcina

                            #Info de nuestro vehículo
    def info(self):
        if self.funciona == True:
            return f"La moto {self.marca} {self.modelo} hace brrrrrr."
        else:
            return f"La moto {self.marca} {self.modelo} no hace brrrrr."

                             #Depuración
    def __repr__(self):
        return f"Moto: {self.marca}, {self.modelo}, {'encendida' if self.funciona == True else 'Apagada'}"

class Coche(Vehículo):
    def __init__(self, marca: str, modelo: str):  # Constructor de moto
        self.marca = marca
        self.modelo = modelo
        self.funciona = False

    @property
    def ruedas(self):
        return 4


    def arrancar(self):
        if self.funciona == False:
            self.funciona = True
            return self.funciona


    def detener(self):
        if self.funciona == True:
            self.funciona = False
            return self.funcina


    def info(self):
        if self.funciona == True:
            return f"El coche {self.marca} {self.modelo} hace sutututututut."
        else:
            return f"El coche {self.marca} {self.modelo} no hace no hace sutututututut."

 # Depuración
    def __repr__(self):
        return f"Coche: {self.marca}, {self.modelo}, {'Arrancado' if self.funciona == True else 'Apagado'}"

class Camion(Vehículo):
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.funciona = False

    @property
    def ruedas(self):
        return 6

    def arrancar(self):
        if self.funciona == False:
            self.funciona = True
            return self.funciona

    def detener(self):
        if self.funciona == True:
            self.funciona = False
            return self.funcina
                            #Info de nuestro vehículo
    def info(self):
        if self.funciona == True:
            return f"El camión {self.marca} {self.modelo} goes brrrrrr."
        else:
            return f"El camión {self.marca} {self.modelo} goent brrrrr."

                           #Depuración
    def __repr__(self):
        return f"Camión: {self.marca}, {self.modelo}, {'Arrancado' if self.funciona == True else 'Detenido'}"

def main():
    vespino = Moto("Vespa", "La del anuncio de ferrari")
    print(vespino.info())
    vespino.arrancar()
    print(vespino.info())
    cochaso = Coche("Toyota", "Supra")
    print(cochaso.info())
    cochaso.detener()
    cochaso.arrancar()
    print(cochaso.info())
    Camionsillo = Camion("Uno", "Cualquiera")
    print(Camionsillo.info())
    Camionsillo.detener()
    Camionsillo.arrancar()
    print(Camionsillo.__repr__())
main()