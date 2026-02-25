import xml.etree.ElementTree as ET
import xml.dom.minidom
import json
import datetime

class PrecioInvalidoError(Exception):       #Control de errores
    pass

class Vehiculo():       #Clase Madre
    def __init__(self, matricula: str, marca: str, precio_base_dia: float):
        if precio_base_dia < 0:     #Control de errores, el precio no puede ser negativo
            raise PrecioInvalidoError('El precio base de dia no puede ser negativo')
        self.precio_base_dia = float(precio_base_dia)
        self.matricula = matricula
        self.marca = marca

    def calcular_precio(self):
        return self.precio_base_dia

    def __str__(self):
        return f'{self.matricula}, {self.marca}'

class VehiculoDias(Vehiculo):
    def __init__(self, matricula: str, marca: str, precio_base_dia: float):
        super().__init__(matricula, marca, precio_base_dia)
        if dias_alquiler <= 0:      #Control de errores, no queremos días negativos o 0, si no, no se alquila
            raise PrecioInvalidoError('Los días de alquiler no pueden ser 0 o negativos')
        self.dias_alquiler = dias_alquiler

    def calcular_precio(self): #Sobreescribimos el metodo para calcular el precio
        return self.precio_base_dia * self.dias_alquiler

class VehiculoPremium(Vehiculo):
    def __init__(self, matricula: str, marca: str, precio_base_dia: float):
        super().__init__(matricula, marca, precio_base_dia)
        if dias_alquiler <= 0:      #Control de errores, no queremos días negativos o 0, si no, no se alquila
            raise PrecioInvalidoError('Los días de alquiler no pueden ser 0 o negativos')
        self.dias_alquiler = dias_alquiler
        self.extra = extra

    def calcular_precio(self): #Sobreescribimos el metodo para calcular precio.
        extras = 0
        for ext in self.extra.values():
            extras += ext
        total = (self.precio_base_dia + extras) * self.dias_alquiler
        return total


def menu(): #Creamos la función menú en el caso de querer traducirlo, que somos muy internacionales
    print('--- MENÚ ---')
    print('1. Añadir vehículos.')
    print('2. Añadir clientes.')
    print('3. Mostrar vehículos disponibles.')
    print('4. Alquilar.')
    print('5. Salir.')


def main():
    while True: #Iniciamos el bucle del menú
        menu()     #imprimimos el menú
        opcion = input('Ingrese su opcion: ')
        match opcion:
            case '1':     #Añadimos un vehículo por días
                try:
                    matricula= input('Ingrese la matricula: ')
                    marca = input('Ingrese la marca: ')
                    precio_base_dia = float(input('Ingrese el precio: '))
                    bicicleta =VehiculoDias(matricula, marca, precio_base_dia)
                    """Insertar linea para añadir a XML"""
                except ValueError:
                    print(f'Valor incorrecto, inténtelo de nuevo.')
                except PrecioInvalidoError as e:        #Control de errores
                    print(e)
                try:     #Añadimos un vehículo Premium
                    matricula = input('Ingrese la matricula: ')
                    marca = input('Ingrese la marca: ')
                    precio_base_dia = float(input('Ingrese el precio: '))
                    patinete = VehiculoPremium(matricula, marca, precio_base_dia)
                    """Insertar linea para añadir a XML"""
                except ValueError:
                    print('Valor incorrecto, inténtelo de nuevo')
                except PrecioInvalidoError as e:
                    print(e)
            case '2':
                """Código para añadir clientes"""

            case '3': """Código para mostrar los coches disponibles"""

            case '4':     """Código para alquilar"""

            case '5':     #Salida
                print('...Saliendo...')
                break
            case _:
                print('Error, intentelo de nuevo')



if __name__ == '__main__':
    main()