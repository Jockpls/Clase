def contar_digitos(n):
    if n < 0:
        return False
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n/10)

def main():
    n = int(input("Ingresa un numero: "))
    print(contar_digitos(n))

main()