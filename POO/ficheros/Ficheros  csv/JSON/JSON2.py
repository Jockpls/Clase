import json

with open('datos.json') as file:
    data = json.load(file)
    for line in data:
        print(f'[{line['ID']}] {line['Nombre']}, {line['Email']} ')