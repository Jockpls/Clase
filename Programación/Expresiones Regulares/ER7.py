"""Valida un email con estructura:
usuario@dominio.com
Condiciones:
- Usuario: letras, números, punto o guion bajo
- Dominio: solo letras
- Extensión: entre 2 y 4 letras"""
import re
correo = input("Ingrese su correo: ")

if re.fullmatch(r"[A-Za-z0-9\S]+@[A-Za-z]+\.[a-z]{2,4}$", correo):
    print('Correcto')
else:
    print('Incorrecto')