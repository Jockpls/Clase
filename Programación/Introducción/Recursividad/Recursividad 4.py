def invertir(cadena):
    if cadena == "":
        return ""
    else:
        return invertir(cadena[1:]) + cadena[0]



def main():
    cadena = "123456789"
    print(invertir(cadena))

main()