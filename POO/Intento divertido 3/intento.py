from logging import exception


class Empleado():
    def __init__(self, nombre: str, salariobase: float):
        self.nombre = nombre
        if salariobase <= 0:
            raise CantidadIncorrecta(f'La cantidad introducida es erronea')
        self.__salariobase = salariobase

    @property
    def salariobase(self):
        return salariobase

    @salariobase.setter
    def salariobase(self):
        pass

    def calcular_salario(self):
        return self.__salariobase

    def __str__(self):
        return f'{self.nombre}, {self.__salariobase}'

class EmpleadoHoras(Empleado):
    def __init__(self, horas_trabajadas: float, precio_hora: float):
        super().__init__(nombre)
        if precio_hora <= 0 or horas_trabajadas <= 0:
            raise CantidadIncorrecta(f'La cantidad introducida es erronea')
        self.precio_hora = precio_hora
        self.__horas_trabajadas = horas_trabajadas

    @property
    def horas_trabajadas(self):
        return self.__horas_trabajadas

    def calcular_salario(self, horas_trabajadas, precio_hora):
        salario = precio_hora * horas_trabajadas
        return f'{salario}€.'

    def __str__(self):
        return f'{self.nombre}, {self.precio_hora}, {self.__horas_trabajadas}'

class EmpleadoFijo(Empleado):
    def __init__(self, complementos: dict):
        super().__init__(nombre, salariobase)
        self.__complementos[conceptos] = complementos

        def sueldo(self, complementos):
            for conceptos in complementos:
                sum_compl = 0
                sum_compl += complementos[conceptos]
                salario = sum_compl + salariobase
                return f'{salario}€.'

class CantidadIncorrecta(exception):
    pass

def menu():
    while True:
        print(f'1.Añadir Empleado.')
        print(f'2.Mostrar salario.')
        print(f'3.Salir.')
        option = int(input('¿Qué desea hacer? '))
        match option:
            case 1:

            case 2:

            case 3:
                break
def main():
    employee[id_empleado] = empleado1
    menu()