"""Valida teléfonos que:
- Tengan 9 cifras
- Empiecen por 6, 7 o 9"""
import re

telefono = input("Ingrese su telefono: ")
if re.fullmatch('6[0-9]{8}|7[0-9]{8}|9[0-9]{8}', telefono):
    print('Correcto')
else:
    print('Incorrecto')