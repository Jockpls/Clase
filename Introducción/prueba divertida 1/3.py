n = int(input("Dime el tamaño de tu matriz: "))
rows = n
columns = n
matriz = []
for i in range(rows):
    fila = []
    for j in range(columns):
        num = int(input(f"Introduce un número [{i}{j}]: "))
        fila.append(num)
    matriz.append(fila)
suma_fila = 0
for i in matriz:
    i = int(input(f"¿Qué fila quieres sumar? de 0 a {n-1} "))
    for j in matriz[i]:
        suma_fila +=j
    print(f"La suma es {suma_fila}")
    break