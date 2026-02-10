import csv

with open('alumnos2.csv', 'rt') as csvfile:
    line = csv.DictReader(csvfile, delimiter=';')
    for linea in line:
        valor = int(linea['Edad'])
        if valor >= 18:
            print(linea)
