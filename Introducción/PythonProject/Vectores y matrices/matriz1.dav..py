matriz = []
rows = 3
columns = 3
#Bucle para introducir los elementos de la matriz
for i in range(rows):
    fila = []
    for j in range(columns):
        num = int(input(f"Introduce un elemento: [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)

print("Aqui tienes tu matriz")
for fila in matriz:
    print(fila)

for i in range(3):
    suma_fila = 0
    for j in range(3):
        suma_fila += matriz[i][j]
    print(suma_fila)