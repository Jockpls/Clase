class CuentaBancaria():
    def __init__(self):
        self.__saldo = 2

    @property
    def saldo(self):
        return self.__saldo


class CuentaBancaria2():
    def __init__(self):
        self.__saldo = 2

    def get_saldo(self):
        return self.__saldo

def main():
    cuenta1 = CuentaBancaria()
    cuenta2 = CuentaBancaria2()
    print(cuenta1.saldo)
    print(cuenta2.get_saldo())

main()

#Con property se declara como una propiedad o atributo de la clase, y al usar get_saldo se define como una función.