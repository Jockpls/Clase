n = int(input("Dame un tamaño para las columnas y filas de la matriz: "))
row = n
column = n
matriz = []
lista_inversa = []
lista_principal = []

for i in range(row):
    fila = []
    for j in range(column):
        num = int(input(f"Dame elementos: [{i}{j}]= "))
        fila.append(num)
        if n-1==i+j:
            lista_inversa.append(num)
        if i==j:
            lista_principal.append(num)
    matriz.append(fila)
print(f"La matriz es {matriz}, la diagonal principal es {lista_principal} y la diagonal inversa es {lista_inversa}")