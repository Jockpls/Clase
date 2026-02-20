def contar_elementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])


def main():
    lista = [1,2,3,4,5]
    print(contar_elementos(lista))

main()