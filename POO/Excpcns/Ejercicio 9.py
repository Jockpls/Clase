"""Bucle para que se tenga que introducir el valor hasta que sea correcto"""
while True:
    try:
        num = int(input("Introduce un numero entero: "))

    except ValueError:
         print('Error, inténtelo de nuevo')
    else:
        break
    finally:
        print('Ketchup o katsup?')