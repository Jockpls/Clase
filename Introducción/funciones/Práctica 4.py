def palindromo(palabra):
        palabra = palabra.upper()
        palabrainv = palabra[::-1]
        if palabrainv == palabra:
            return True
        else:
            return False

def main():
    palabra = input("Introduce una palabra para comprobar si es un palíndromo: ")
    if palindromo(palabra):
        print("Mu bien cabesa")
    else:
        print("Ni de coña chaval")

main()