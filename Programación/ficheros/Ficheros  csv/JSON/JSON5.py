import json
try:
    with open('datoscorrupt.json', 'r', encoding= 'utf-8') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print('Error al abrir el archivo o formato inválido')
    data = []

validos = []
claves = ['ID','Nombre', 'Email']

for indice, elemento in enumerate(data):
    if isinstance(elemento, dict):
        es_valido = True
        for clave in ['ID', 'Nombre', 'Email']:
            if clave not in elemento:
                es_valido = False

        if es_valido:
            validos.append(elemento)
        else:
            print(f'Error {elemento} no es válido')
    else:
        print('Esto no es un diccionario')
print(validos)