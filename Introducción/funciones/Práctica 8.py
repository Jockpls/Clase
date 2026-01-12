def buscar_elemento(matriz, valor):
    for fila in matriz:
        if valor in fila:
            return True
        else:
            return False


def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    valor = int(input())
    if buscar_elemento(matriz,valor):
        print("Si")
    else:
        print("none")
main()