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
    def __init__(self, matricula: str, marca: str, precio_base_dia: float, dias_alquiler: int):
        super().__init__(matricula, marca, precio_base_dia)
        if dias_alquiler <= 0:      #Control de errores, no queremos días negativos o 0, si no, no se alquila
            raise PrecioInvalidoError('Los días de alquiler no pueden ser 0 o negativos')
        self.dias_alquiler = dias_alquiler

    def calcular_precio(self): #Sobreescribimos el metodo para calcular el precio
        return self.precio_base_dia * self.dias_alquiler

class VehiculoPremium(Vehiculo):
    def __init__(self, matricula: str, marca: str, precio_base_dia: float, dias_alquiler: int, extra: dict):
        super().__init__(matricula, marca, precio_base_dia)
        if dias_alquiler <= 0:      #Control de errores, no queremos días negativos o 0, si no, no se alquila
            raise PrecioInvalidoError('Los días de alquiler no pueden ser 0 o negativos')
        self.dias_alquiler = dias_alquiler
        self.extra = extra

    def calcular_precio(self): #Sobreescribimos el metodo para calcular precio.
        total = self.precio_base_dia * self.dias_alquiler
        for ext in self.extra.values():
            total += ext
        return total


def menu(vehiculos): #Creamos la función menú en el caso de querer traducirlo, que somos muy internacionales
    print('--- MENÚ ---')
    print('1. Añadir vehículos por días.')
    print('2. Añadir vehículo premium')
    print('3. Mostrar Precios')
    print('4. Salir.')


def main():
    vehiculos = {}
    while True: #Iniciamos el bucle del menú
        menu(vehiculos)     #imprimimos el menú
        opcion = input('Ingrese su opcion: ')
        match opcion:
            case '1':     #Añadimos un vehículo por días
                try:
                    matricula= input('Ingrese la matricula: ')
                    marca = input('Ingrese la marca: ')
                    precio_base_dia = float(input('Ingrese el precio: '))
                    dias_alquiler = int(input('¿Por cuántos días se alquila el coche? '))
                    bicicleta =VehiculoDias(matricula, marca, precio_base_dia, dias_alquiler)
                    vehiculos[matricula] = bicicleta    #Añadimos el objeto al diccionario
                except ValueError:
                    print(f'Valor incorrecto, inténtelo de nuevo.')
                except PrecioInvalidoError as e:        #Control de errores
                    print(e)
            case '2':     #Añadimos un vehículo Premium
                try:
                    matricula = input('Ingrese la matricula: ')
                    marca = input('Ingrese la marca: ')
                    dias_alquiler = int(input('¿Por cuántos días se alquila el coche? '))
                    precio_base_dia = float(input('Ingrese el precio: '))
                    extra = {}
                    conceptos = input('¿Quiere contratar algún extra (Enter para salir)? ')
                    while conceptos != '':  #Bucle para añadir conceptos
                        extr = float(input('¿Cuál es el precio del extra?'))
                        if extr < 0:    #No queremos que los conceptos puedan ser negativos
                            raise PrecioInvalidoError('El precio del extra no puede ser negativo')
                        else:
                            extra[conceptos] = extr #Añadimos el extra al diccionario
                            conceptos = input('¿Desea añadir alguno más?')
                    patinete = VehiculoPremium(matricula, marca, precio_base_dia, dias_alquiler, extra)
                    vehiculos[matricula] = patinete #Añadimos el objeto al diccionario
                except ValueError:
                    print('Valor incorrecto, inténtelo de nuevo')
                except PrecioInvalidoError as e:
                    print(e)
            case '3':     #Mostramos precios
                print('--- Calculando los precios ---')
                for matricula, valor in vehiculos.items():
                    print(f'El coche con la matrícula {matricula}, que es del tipo {vehiculos[matricula].__class__.__name__}, tiene un precio de {vehiculos[matricula].calcular_precio()}€ en total.')
            case '4':     #Salida
                print('...Saliendo...')
                break
            case _:
                print('Error, intentelo de nuevo')



if __name__ == '__main__':
    main()