import re

texto = "Hoy tenemos clase de programación en Python"
if re.search("Python", texto):
    print('Sí está')
else:
    print('Mi madre me dijo a mi que cantara y no llorara')