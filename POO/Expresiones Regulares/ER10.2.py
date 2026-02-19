import re

texto = "12/03/2026"
resultado = re.sub("([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})",r"\3-\2-\1", texto)
print(resultado)