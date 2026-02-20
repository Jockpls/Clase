try:
    x1 = float(input("Ingrese un numero: "))
    x2 = float(input("Ingrese otro numero: "))
    print(x1/x2)
#/0 Exception
except ZeroDivisionError:
    print("Error, no se puede dividir por cero")
#NonNumeric Exception
except ValueError:
    print("Error, valores incorrecto")