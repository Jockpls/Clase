import csv
import json

lista_alumnos = []

with open('alumnos.csv', 'rt', encoding = 'utf-8') as file:
    data = csv.DictReader(file)
    for fila in data:
        alumno = {
            'Nombre': fila['Nombre'],
            'Edad': int(fila['Edad']),
            'Curso': fila['Curso'].strip(),
        }
        lista_alumnos.append(alumno)
        print(fila)

with open('alumnos.json', 'w', encoding = 'utf-8') as json_file:
    json.dump(lista_alumnos, json_file)
