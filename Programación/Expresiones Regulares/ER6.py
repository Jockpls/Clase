"""Formato:
1234 ABC
Condiciones:
- 4 números
- Espacio opcional
- 3 letras mayúsculas"""
import re

matricula = input("Ingrese su matricula: ")

if re.fullmatch('[0-9]{4}[ ]?[A-Z]{3}',matricula):
    print('correcto')
else:
    print('incorrecto')