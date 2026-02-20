"""Extraer:
- Nivel
- Fecha
- Hora
- Usuario"""
import re

log = "ERROR 2026-02-17 10:23:45 Usuario admin no autorizado"
print(re.search(r"([A-Z]+)\s([0-9]{4}\W[0-9]{1,2}\W[0-9]{1,2})\s([0-9]{1,2}\W[0-9]{2}\W[0-9]{1,2})\s(Usuario\s[A-Za-z]{0,}\s)", log))