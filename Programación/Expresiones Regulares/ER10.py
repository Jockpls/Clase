import re

texto = "12/03/2026"
fechainglesa = []
regex = re.split("/",texto, maxsplit = 4)
for elemento in regex[::-1]:
    fechainglesa.append(elemento)
patron = "-".join(fechainglesa)
print(patron)