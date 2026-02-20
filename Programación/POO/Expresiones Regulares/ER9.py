"""Extrae todas las fechas en formato dd/mm/aaaa."""
import re

texto = "El examen será el 12/03/2026 y la entrega el 25/04/2026"
print(re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}", texto))