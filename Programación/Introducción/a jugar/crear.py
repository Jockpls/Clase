#Crear programa en el que se pida n alumnos, siendo este el número de filas de la matriz, y 5 notas, nota media alumnos y media asignatura y contar suspensos
n = int(input(f"Dame un número de alumnos"))
rows = n
columns = 5
matriz = []

for i in range(rows):
    fila = []
    for j in range(columns):
        materia = int(input(f"Dame la nota de la materia [{i},{j}]: "))
        fila.append(materia)
    matriz.append(fila)

for fila in matriz:
    print(fila)

promedio = []
for i in range(rows):
    count = 0
    for j in range(columns):
        count += matriz[i][j]
    promedio.append(count/5)
print(promedio)

matriz_resultado =[[0 for _ in range(columns)] for _ in range(rows)] #Para poder jugar con los valores de la matriz sin tenerla creada aún.
                                                                    #Se ejecuta de derecha a izquierda.