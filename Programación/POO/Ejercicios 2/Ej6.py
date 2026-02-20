from abc import ABC, abstractmethod
from beartype import beartype

@beartype
class MetodoPago(ABC):
    @abstractmethod
    def pago(self, cantidad):
        pass

    @abstractmethod
    def __str__(self):
        pass

class TarjetaCredito(MetodoPago):
    def __init__(self, titular: str, tarjeta: str, limite: float):
        self.titular = titular
        self.tarjeta = tarjeta
        self.limite = limite
        self.__dinero = 10000.0

    @property
    def dinero(self):
        return self.dinero

    @dinero.setter
    def dinero(self, dinero):
        self.__dinero = dinero

    def pago(self, cantidad):
        self.limite -= cantidad
        self.__dinero -= cantidad
        if self.limite < 0 or self.__dinero < 0:
            raise ValueError(f"No puedes hacer ese pago")
        else:
            return self.__dinero

    def __str__(self):
        return f"{self.titular} tiene disponible {self.limite}€ para pagar con tarjeta de {self.tarjeta} y le queda un saldo de {self.__dinero}€"

class Bizum(MetodoPago):
    def __init__(self, titular: str, cuenta: str, maximo: float, dinero: float):
        self.titular = titular
        self.cuenta = cuenta
        self.maximo = maximo
        self.__dinero = dinero

    @property
    def dinero(self):
        return self.__dinero
    @dinero.setter
    def dinero(self, dinero):
        self.__dinero = dinero

    def pago(self, cantidad):
        self.maximo -= cantidad
        self.__dinero -= cantidad
        if self.maximo < 0 or self.__dinero < 0:
            raise ValueError(f"No puedes pasar más de {self.maximo}.")
        else:
            return self.__dinero

    def __str__(self):
        return f"A {self.titular} en su cuenta {self.cuenta} le queda {self.__dinero}€"

class Paypal(MetodoPago):
    def __init__(self, titular: str, saldo: float, correo: str):
        self.titular = titular
        self.__saldo = saldo
        self.correo = correo

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def pago(self, cantidad):
        self.__saldo -= cantidad
        if self.__saldo < 0:
            raise ValueError (f'No puedes tener saldo negativo.')
        else:
            return self.__saldo

    def __str__(self):
        return f'A {self.titular} le queda un saldo de {self.__saldo}€ en su cuenta con el correo {self.correo}'

def main():
    pagotarjeta = TarjetaCredito("Jose Carlos", "Debito",1000)
    cantidad = float(input('¿Cuál es el importe? '))
    pagotarjeta.pago(cantidad)
    print(pagotarjeta)
    bizum = Bizum("Jose Carlos", "Joven", 500, 8000)
    cantidad = float(input('¿Cuánto vas a pasar? '))
    bizum.pago(cantidad)
    print(bizum)
    paypal = Paypal("Elon Musk", 500000000, 'soymurico@riquisimo.com')
    canitdad = float(input('¿De cuánto va a ser la transacción? '))
    paypal.pago(canitdad)
    print(paypal)
main()