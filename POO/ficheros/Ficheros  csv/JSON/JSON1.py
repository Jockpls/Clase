import json
datos = [{
    'ID': 'Joseca',
    'Nombre':'Jose Carlos',
    'Email': 'mentira@gmail.com'
},
{
    'ID':'Paco',
    'Nombre':'Jose Manuel',
    'Email':'verdad@gmail.com'
},
{
    'ID': 'Davilillo',
    'Nombre': 'David',
    'Email': 'davirs@gmail.com'
}
]
with open('datos.json', 'wt') as json1:
    json.dump(datos, json1)

print('Archivo creado correctamente')