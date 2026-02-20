def buscar(lista, valor):
    if len(lista) == 0:
        return False
    if lista[0] == valor:
        return True

    return buscar(lista[1::], valor)

def main():
    lista = [1,2,3,4,5]
    valor = int(input("Ingresa un numero: "))
    print(buscar(lista, valor))

main()