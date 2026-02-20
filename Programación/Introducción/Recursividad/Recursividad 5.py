def suma_lista(lista):
    if len(lista) == 0:
        return False
    else:
        return lista[0] + suma_lista(lista[1:])


def main():
    lista = [6,2,3,4,5]
    print(suma_lista(lista))

main()