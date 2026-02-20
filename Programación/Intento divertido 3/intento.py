class Empleado():
    def __init__(self, id_empleado: int, nombre: str, salariobase: float):
        self.nombre = nombre
        self.id_empleado = id_empleado
        if salariobase <= 0:
            raise CantidadIncorrecta(f'La cantidad introducida es erronea')
        self.__salariobase = salariobase

    @property
    def salariobase(self):
        return self.__salariobase

    @salariobase.setter
    def salariobase(self):
        pass

    def calcular_salario(self):
        return self.__salariobase

    def __str__(self):
        return f'{self.id_empleado}, {self.nombre}, {self.__salariobase}'

class EmpleadoHoras(Empleado):
    def __init__(self, horas_trabajadas: float):
        super().__init__(id_empleado ,nombre, salariobase)
        self.__horas_trabajadas = horas_trabajadas

    @property
    def horas_trabajadas(self):
        return self.__horas_trabajadas

    def calcular_salario(self, horas_trabajadas, salariobase):
        salario = precio_hora * horas_trabajadas
        return f'{salario}€.'

    def __str__(self):
        return f'{self.nombre}, {self.precio_hora}, {self.__horas_trabajadas}, {calcular_salario(self.horas_trabajadas, self.precio_hora)}'

class EmpleadoFijo(Empleado):
    def __init__(self):
        super().__init__(id_empleado, nombre, salariobase)
        self.complementos[concepto] = {cantidad}

    def sueldo(self, complementos):
        sum_compl = 0
        for i in self.complementos:
            sum_compl += i
        salario = sum_compl + salariobase
        return f'{salario}€.'

    def __str__(self):
        return f'{self.id_empleado}, {self.nombre}, {self.sueldo()}'

class SalarioInvalidoError(Exception):
    pass

def menu():
    while True:
        print(f'1.Añadir Empleado.')
        print(f'2.Mostrar salario.')
        print(f'3.Salir.')
        option = int(input('¿Qué desea hacer? '))
        match option:
            case 1:
                #Añadir Empleados al diccionario
                id = int(input('Introduce el id del empleado: '))
                nombre_empleado = input('Introduce el nombre: ')
                salariobase = float(input('Introduce el salario: '))
                empleado1 = Empleado(id, nombre_empleado, salariobase)
                tipo = int(input('Introduce el tipo de empleado, 1 fijo, 2 horas: '))
                if tipo == 1:
                    empleado2 =
                elif tipo == 2:
                    horas = float(input('Introduce la horas trabajadas: '))
                    employee1 = EmpleadoHoras(empleado1, horas)
                base_empleados = employee1
            case 2:
                #Mostrar salarios
                for i in base_empleados:
                    print(i)
            case 3:
                break
            case _:
                return f'Incorrecto, intentelo de nuevo'
def main():
    try:
        base_empleados= {}
        menu()

    except ValueError:
        return f'Cantidad incorrecta, intentelo de nuevo'


if __name__ == '__main__':
    main()