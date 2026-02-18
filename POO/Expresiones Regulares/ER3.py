import re

texto = "Ana y Luis estudian en Córdoba"

print(re.findall("[A-ZÁÉÍÓÚ][a-záéíóú]+", texto))