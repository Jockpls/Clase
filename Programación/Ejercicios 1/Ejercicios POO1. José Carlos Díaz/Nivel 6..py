class Cliente():                    #Creamos la clase cliente
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"


class CuentaBancaria(Cliente):             #Creamos la clase CuentaBancaria

    def __init__(self, cantidad, nombre):
        super().__init__(nombre)
        self.__cantidad = float(cantidad)         #La cantidad de dinero es algo privado

    @property
    def cantidad(self):                   #Definimos la propiedad cantidad
        return self.__cantidad

    @cantidad.setter                        #Definimos el setter
    def cantidad(self, cantidad):
        pass

    def depositar(self, ingreso):                                    #Metodo para ingresar
        self.__cantidad += ingreso

    def retirar(self, retiro):                                       #Metodo para retirar
            if self.__cantidad < retiro:
                return False
            else:
                self.__cantidad -= retiro
                return True

    def __str__(self):                                                  #Mostramos los datos de la cuenta del cliente
        return f"La cantidad en la cuenta de {self.nombre} es {self.__cantidad}"

def main():
    cliente1 = Cliente("Joseca")                                            #Creamos un cliente
    cuenta1 = CuentaBancaria(0, cliente1)                    #Creamos una cuenta
    while True:                                                             #Menú para ingresar, retirar o ver el saldo.
        accion = int(input("1 para Depositar, 2 para Retirar, 3 para ver el saldo, 4 para terminar. "))
        match accion:
            case 1:
                ingreso = float(input("¿Cuánto desea ingresar? "))
                cuenta1.depositar(ingreso)
            case 2:
                retiro = float(input("¿Cuánto desea retirar? "))
                while cuenta1.retirar(retiro) == False:                                             #Comprobación de errores, no queremos tener saldo negativo.
                    retiro = float(input("No puede tener saldo negativo, inténtelo de nuevo. "))
                    cuenta1.retirar(retiro)
            case 3:
                print(cuenta1)
            case 4:
                print(f"Gracias por contar nosotros {cliente1.nombre}.")
                break
main()