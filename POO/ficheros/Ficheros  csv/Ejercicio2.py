lector = open('alumnos.csv', 'rt')
line = lector.readlines()
for linea in line[1:]:
    datos = linea.split(',')
    print(f'Nombre: {datos[0]}| Edad: {datos[1]}| Curso: {datos[2]}')
lector.close()