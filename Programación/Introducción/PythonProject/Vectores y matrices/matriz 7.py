tamaño = int(input("Dame el tamaño de la matriz"))
rows = tamaño
columns = tamaño
matriz = []
matriz2 = []
matriz3 = []
#Hacemos la primera matriz
for i in range(rows):
    fila = []
    for j in range(columns):
        nums = int(input("Números para la matriz"))
        fila.append(nums)
    matriz.append(fila)
print("Aqui tienes tu matriz")
for fila in matriz:
    print(fila)
print("vamos con la segunda matriz")
#Hacemos la segunda matriz
for i in range(rows):
    fila = []
    for j in range(columns):
        nums = int(input("Números para la matriz"))
        fila.append(nums)
    matriz2.append(fila)
print("Aqui tienes tu matriz")
for fila in matriz2:
    print(fila)

#Multipliquemos las matrices
for i in range(tamaño):
    fila = []
    for j in range(tamaño):
        suma = 0
        for k in range(rows):
            suma +=matriz[i][k]*matriz2[k][j]
        fila.append(suma)
    matriz3.append(fila)

    print("Aqui tienes tu matriz")
    for fila in matriz3:
        print(fila)

