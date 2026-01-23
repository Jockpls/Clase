import csv
import os.path
import sys

fichero = input('Introduce el nombre del fichero: ')

if not os.path.exists(fichero):  # comprobamos que el fichero existe
    print(f"El fichero {fichero} no existe. Terminamos...", file=sys.stderr)
    exit(1)


try:
    with open(fichero, 'rt') as file:
        linea = file.readlines()
        print(linea)
except FileNotFoundError:
    print('El fichero no existe')