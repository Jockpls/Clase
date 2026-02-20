class CuentaBancaria:

    def __init__(self, saldo):
        if saldo < 0:
            raise ValueError(f"No puedes tener un saldo negativo")
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad
        return self.__saldo

    def retirar(self, cantidad):
        self.__saldo -= cantidad
        if self.__saldo < 0:
            raise ValueError(f"No puedes tener un saldo negativo")
        else:
            return self.__saldo

    def mostrar(self):
        print(self.__saldo)

def main():
    cuenta = CuentaBancaria(0)
    cantidad = int(input("¿Cuánto quieres ingresar? "))
    cuenta.depositar(cantidad)
    cantidad = int(input("¿Cuánto quieres retirar? "))
    cuenta.retirar(cantidad)
    cuenta.mostrar()

main()
