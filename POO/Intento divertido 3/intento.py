class Empleado():
    def __init__(self, nombre: str, salariobase: float):
        self.nombre = nombre
        self.__salariobase = salariobase

        @property
        def salariobase(self):
            return salariobase

        @salariobase.setter
        def salariobase(self)


class EmpleadoHoras(Empleado):
    def __init__(self, horas_trabajadas: float, precio_hora: float):
        super().__init__(self, nombre, salariobase)




class EmpleadoFijo(Empleado):