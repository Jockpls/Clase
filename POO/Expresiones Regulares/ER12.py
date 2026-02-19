"""Validar contraseña que tenga:
- Mínimo 8 caracteres
- Al menos una mayúscula
- Una minúscula
- Un número
- Un símbolo"""
import re

passw = input('Introduce una contraseña: ')
if re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w])[^\s]{8,}$", passw):
    print('Correcto')
else:
    print('Incorrecto')