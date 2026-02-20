import re

texto = "El aula 23 tiene 18 ordenadores y 2 impresoras"

print(re.findall('[0-9]+', texto))
print(re.findall(r'\d+', texto))