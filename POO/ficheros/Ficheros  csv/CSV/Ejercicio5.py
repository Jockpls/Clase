import csv

with open('alumnos2.csv', 'rt') as csvfile:
    line = csv.DictReader(csvfile, delimiter=';')
    for linea in line:
        try:
            valor = int(linea['Edad'])
            print(linea)
        except ValueError:
            print('Illo que haces?')
            continue
