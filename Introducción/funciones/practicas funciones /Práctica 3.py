def promedio_matriz(matriz):
    n = 0
    contador = 0
    for i in matriz:
        for j in i:
            n += j
            contador += 1
    print(f"El primer promedio es {n/contador}")


def promedioalintroducir():
    rows = int(input("Introduce el tamaño de las filas de tu matriz: "))
    columns = int(input("Introduce el tamaño de las columnas de tu matriz: "))
    contador = 0
    sumador = 0
    matriz = []
    for i in range(rows):
        fila = []
        for j in range(columns):
            numero = int(input(f"Introduce un número [{i}][{j}]: "))
            sumador += numero
            contador += 1
            fila.append(numero)
        matriz.append(fila)
    promedio = sumador / contador
    print(f"El segundo promedio es {promedio:.2f}")

def main():
    #Primer método en el caso de que tengamos una matriz ya dada
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    promedio_matriz(matriz)

    print(f"\nVamos con el segundo método.\n")

    #Método en el caso de que tengamos que introducir la matriz
    promedioalintroducir()




main()
