class Vehiculo():

    def __init__(self, marca, ruedas):
        self.marca = marca
        self.ruedas = ruedas

class bicicleta(Vehiculo):
    def __init__(self, marca, ruedas, tipo):
        super().__init__(marca, ruedas)
        self.tipo = tipo

    def mostrar(self):
        print(f"La marca es {self.marca}, las ruedas son {self.ruedas} y el tipo es {self.tipo}")

def main():
    biciculo = bicicleta(marca = "A tomar por", ruedas = "cleta la ", tipo = "biciculo")
    biciculo.mostrar()


main()