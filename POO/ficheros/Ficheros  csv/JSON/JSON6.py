import json

try:
    with open('datos.json', 'r') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print('Error al abrir el archivo')

if data:
    mail = input('Ingrese el correo: ')
    for usuario in data:
        if usuario.get('Email') == mail:
            print(usuario)
        else:
            print('No se encontró al usuario')