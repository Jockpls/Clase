class CuentaBancaria():
    def __init__(self, __saldo):
        self.__saldo = 2

    def __str__(self):
        return self.__saldo

class CuentaJoven(CuentaBancaria):
    def __init__(self, saldo):
        self.__saldo = saldo

    def __str__(self):
        return self.__saldo

class CuentaJoven2(CuentaBancaria):
    def __init__(self):
        super().__saldo

    def __str__(self):
        return self.__saldo

def main():
    cuenta1 = CuentaBancaria("2")
    cuenta2 = CuentaJoven("5")
    cuenta3 = CuentaJoven2()
    print(cuenta3)

main()

#Si yo utilizo el atributo privado en cada cuenta, aunque se llamen igual, al pertenecer a una clase, no se sobreescribe, ni aun heredandolo
#Los atributos privados no se comparten