def clasificar(lista):
    listapares = []
    listaimpares = []
    for i in lista:
        if i%2 == 0:
            listapares.append(i)
        else:
            listaimpares.append(i)
    print(listapares)
    print(listaimpares)
def main():
    lista = [1,2,3,4,5,6,7,8,9]
    clasificar(lista)

main()