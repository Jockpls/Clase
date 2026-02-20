#Declaramos las variables para la matriz
n = int(input("Dime el tamaño de tu matriz: "))
rows = n
columns = n
matriz = []

#Aquí hacemos la matriz
for i in range(rows):
    fila = []
    for j in range(columns):
        num = int(input(f"Dame elementos: [{i}{j}]= "))
        fila.append(num)
    matriz.append(fila)

#Hacemos la matriz traspuesta
matrizin = []
for i in range(rows):       #Para las filas, la variable i
    fila = []
    for j in range(columns): #Para las columnas, la variable j
        fila.append(matriz[j][i]) #introducimos en fila la matriz del reves
    matrizin.append(fila)

print("Esta es tu matriz")
for fila in matriz:
    print(fila)

print("Esta es tu matriz traspuesta")
for fila in matrizin:
    print(fila)