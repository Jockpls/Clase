"""
Extraer:
- Nombre de la etiqueta
- Contenido"""
import re
texto = "<h1>Título</h1><p>Contenido</p>"
regex = re.findall(r"<[^>]*>([^<]*)</[^>]*>",texto)
print(regex)