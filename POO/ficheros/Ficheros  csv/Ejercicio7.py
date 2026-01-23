import csv
with open('alumnos2.csv') as media:
    linea = DictReader(media)
    for line in linea:
        