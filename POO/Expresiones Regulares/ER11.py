"""DNI de entrada:
12345678Z
Mostrarlo como:
******78Z"""
import re

dni = "12345678Z"
print(re.sub("[0-9]{6}", "*"*6, dni))