"""Validar direcciones tipo:
192.168.1.1
(Opción avanzada: validar que cada bloque esté entre 0 y 255)."""
import re

try:
    ip = "392.168.1.1"
    regex = re.search(r"([0-9]{1,3})\W([0-9]{1,3})\W([0-9]{1,3})\W([0-9]{1,3})",ip)
    for grupo in regex.groups():
        numero = int(grupo)
        if not (numero >= 0 and numero <= 255):
            raise ValueError
    print('Dirección IP válida')
except ValueError:
    print('Dirección IP incorrecta')