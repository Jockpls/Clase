def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

def main():
    base = int(input("Dame una base: "))
    exponente = int(input("Dame un exponente: "))
    print(potencia(base, exponente))

main()