import csv
from collections import Counter

total = 0
edadmedia = 0
cursos = Counter()
with open('alumnos2.csv') as linea:
    linea = csv.DictReader(linea, delimiter = ';', quotechar='"')
    for row in linea:
        try:
            edad = int(row['Edad'])
        except ValueError:
            print(f'{row} invalida, continuamos')
            continue
        edadmedia += edad
        total += 1
        cursos[row["Curso"]] += 1
if total == 0:
    print('No hay filas válidas')
else:
    edadmedia = float(edadmedia/total)
    curso_mas_frecuente =cursos.most_common(1)[0][0]
    print(f'Filas válidas: {total}')
    print(f'Curso más frecuente: {curso_mas_frecuente}')
    print(f'La edad media es {edadmedia}')


