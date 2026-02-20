def suma_columnas(matriz):
    columns = 3
    rows = 3
    suma_columnas = []
    for j in range(columns):
        sumador = 0
        for i in range(rows):
            sumador += matriz[i][j]
        suma_columnas.append(sumador)
    print(suma_columnas)


def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    suma_columnas(matriz)

main()