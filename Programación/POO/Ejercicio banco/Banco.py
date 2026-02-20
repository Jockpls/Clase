'''Ejercicio de banco, dos clases, sacar, ingresar, saldo actual, ultimos movimientos'''
from datetime import date, time, datetime       #Quiero saber fecha y hora de las transacciones así cómo la edad.
from random import randint  #Para hacer IBAN aleatorios

global base

#Creamos la clase cuenta
class Cuenta():
    def __init__(self,  titular: str, saldo = 0):
        self.__iban: iban
        self.__saldo = saldo
        self.__titular: titular #Utilizamos el titular para unir al objeto cuenta con el objeto cliente
        base.add(titular, self.__iban)
        self.autorizado: []
        self.__movimientos: []

    @property
    def titular(self):
        return self.__titular
    @titular.setter                 #Getter y setter de titular
    def titular(self, Cliente):
        self.__titular = Cliente

    @property
    def saldo(self):
        return self.__saldo

    @property
    def iban(self):
        return self.__iban
    @iban.setter                    #El iban será aleatorio en nuestro caso.
    def iban(self):
        limite_inf = 10 ** 11
        limite_sup = 10 ** 12
        self.__iban = randint(limite_inf, limite_sup)

    @property
    def movimientos(self):
        return self.__movimientos

    def ingresar(self, cantidad):       #Función para añadir saldo
        self.__saldo += cantidad


    def retirar(self, cantidad):            #Función para sacar dinero para ''comer''
        if cantidad >= self.__saldo:
            return f'No se puede retirar esa cantidad.'
        else:
            self.__saldo -= cantidad
            return f'El saldo actual es de {self.__saldo}'

    def enviar(self, persona1):         #Aquí te vigila hacienda cuidaito
        for i in self.autorizado:
            for f in i:
                if f == persona1:
                    cantidad = int(input(f'¿Cuánto desea envíar?'))





    def __str__(self):
        return f'El saldo es {self.__saldo}, el titular es {self.__titular}, los autorizados son {self.autorizado} y los movimientos son {self.__movimientos}'
class BasedeCuentas():
    def __init__(self):
        self.__base = {}
    @property
    def base(self):
        return self.__base

    def add(self,titular, iban):
        self.base[titular] = iban

class Cliente():                        #Objeto cliente
    def __init__(self, nombre: str, documento: str, Fnacimiento: date):
        self.__documento = documento
        self.nombre: nombre
        self.fnacimiento: Fnacimiento

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, documento):
    #Primero declaramos variables y el diccionario a utilizar.
        data_nie = str.maketrans("XYZ","012")
        documento = self.__documento
        documentomayus = documento.upper()
        if len(documentomayus) == 9:
            if documentomayus[1:8].isdigit() == False:
                return f"Documento mal introducido"
            elif documentomayus[8].isalpha() == False:
                return f"Documento mal introducido, el último caracter no es una letra"
            elif documentomayus[0].isdigit() == False and documentomayus[0] != "X" and documentomayus[0] != "Y" and documentomayus[0] != "Z":
                return f"Documento mal introducido"
            else:
                for i in range(1):
                    i = documentomayus[0:8].translate(data_nie)

                dni_letra = documentomayus[8]
                dni = int(i)    ##Convertimos la letra del documento en un número

                # Esta es la operación para ver si el documento se ha introducido bien.
                calculoletra = dni % 23
                lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L","C", "K", "E"]
                if dni_letra == lista[calculoletra]:
                        return f"La letra del documento es correcta"
                else:
                        return f"la letra del documento es incorrecta debería ser {lista[calculoletra]}"
        else:
            return f"El documento tiene que tener 9 caracteres"

    def edad(self, fnacimiento):
        edad = fnacimiento-date
        if edad > 18:
            return True
        else:
            return False

def menu():
    while menu != 5:
        print(f'1. Abrir cuenta.')
        print(f'2. Ingresar.')
        print(f'3. Retirar.')
        print(f'4. Enviar dinero.')
        print(f'5. Consultar estado de la cuenta y movimientos.')
        print(f'6. Salir')
        menu = int(input(f'¿Qué desea hacer?'))
        match menu:
            case 1:
                name = input(f'¿Cuál sería el nombre del titular de la cuenta?\n ')
                document = input(f'¿Cuál es el documento de identidad?\n ')
                nacer = input(f'¿Cuál es su fecha de nacimiento')
                edad = date - nacer
                cliente1 = Cliente(name, document, edad)
                saldo = float(input(f'Quiere hacer algún ingreso en su cuenta? Si no, su saldo inicial será 0.'))
                cuenta1 = Cuenta(cliente1, saldo)

            case 2:
                clientecondinero = input('¿Quién es el titular de la cuenta a la que ingresar? ')
                cantidad = float(input(f'¿Cuánto desea ingresar? '))
                cuenta1.ingresar(cantidad)
            case 3:

            case 4:
                persona1
            case 5:

            case _:
                print(f'Opción incorrecta, inténtelo de nuevo.')




def inicializar_cuenta():
    '''Inicialicemos las cuentas y clientes'''


if __name__ == '__main__':
banco = inicializar_cuenta()
menu(banco)