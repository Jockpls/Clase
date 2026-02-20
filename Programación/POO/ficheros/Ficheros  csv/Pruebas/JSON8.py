import json
import csv

with open('alumnos.json', 'r') as json_file:
    alumnos = json.load(json_file)

with open('usuarios.csv', 'wt') as csv_file:
    user = csv.writer(csv_file, delimiter=';', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    user.writerow(['Nombre', 'Edad', 'Curso'])
    for alumno in alumnos:
        fila = [alumno['Nombre'], alumno['Edad'], alumno['Curso']]
        user.writerow(fila)