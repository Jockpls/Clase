rows = 3
columns = 3
matriz = []

#Bucle para introducir los elementos de la matriz
for i in range(rows):
    fila = []
    for j in range(columns):
        num = int(input(f"Introduce un elemento: [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)
for fila in matriz:
    print(fila)

#Bucle para sumar las filas
for i in range(rows):
    sum_row = 0
    for j in range(columns):
        sum_row += matriz[i][j]
    print(f"La suma de la fila {i} es: {sum_row}")
#Bucle para sumar las columnas
for j in range(rows):
    sum_column = 0
    for i in range(columns):
        sum_column += matriz[i][j]
    print(f"La suma de la columna {j} es: {sum_column}")