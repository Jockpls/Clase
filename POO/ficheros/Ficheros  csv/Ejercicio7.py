import csv

with open('alumnos2.csv') as linea:
    linea = csv.DictReader(linea, delimiter = ';')
    total = 0
    edadmedia = 0
    for row in linea:
        try:
            edad = int(row['Edad'])
            edadmedia += edad
            total += 1
        except ValueError:
            print('Fila invalida, continuamos')
            continue

    edadmedia = float(edadmedia/total)
    print(f'La edad media es {edadmedia}')


