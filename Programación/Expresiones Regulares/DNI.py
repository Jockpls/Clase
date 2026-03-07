"""Analizar DNI"""
import re

dni = input("Ingrese DNI: ")
dni = dni.upper()

if re.fullmatch(r"\d{8}[A-HJ-NP-TV-Z]$", dni):
    print('illo')
else:
    print('no illo')