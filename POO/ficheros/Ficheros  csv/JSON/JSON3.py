import json

with open('datos.json', 'r') as file:
    usuarios = json.load(file)

Id = input('Ingrese el ID de la persona: ')
Nombre = input('Ingrese el nombre de la persona: ')
Email = input('Ingrese el email de la persona: ')
datos = {
    'Id': Id,
    'Nombre': Nombre,
    'Email': Email
}
usuarios.append(datos)
with open('datos.json', 'w') as file:
    json.dump(usuarios, file)

print('El proseso ha fuido un esito')