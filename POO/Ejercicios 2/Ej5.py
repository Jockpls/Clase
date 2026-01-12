from abc import ABC, abstractmethod
from beartype import beartype

@beartype
class Empleado(ABC):
    @property
    def salario(self):
        pass

    def __str__(self):
        pass

class EmpFijo(Empleado):
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def __str__(self):
        return f'El salario de {self.nombre} es {self.__salario}€ al mes'

class EmpHoras(Empleado):
    def __init__(self, nombre: str, horas: float, sueldo: float):
        self.nombre = nombre
        self.horas = horas
        self.sueldo = sueldo
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self):
        self.__salario = self.sueldo * self.horas

    def __str__(self):
        return f'El sueldo de {self.nombre} tras trabajar {self.horas} horas es de {self.__salario}'

class Comisionista(Empleado):
    def __init__(self, nombre: str, ventas: int, comision: float):
        self.nombre = nombre
        self.ventas = ventas
        self.comision = comision
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self):
        self.__salario = self.comision * self.ventas

    def __str__(self):
        return f'El salario de este mes de {self.nombre} es de {self.__salario}€ tras hacer {self.ventas}, siendo la comisión de {self.comision}€ por venta'

def main():
    fijo = EmpFijo('José Carlos', 3000)
    print(fijo)
    horas = EmpHoras('Paco', 89.36, 15.24)
    print(horas)
    comercial = Comisionista('Pedro', 63,36.99)
    print(comercial)


if __name__ == '__main__':
    main()