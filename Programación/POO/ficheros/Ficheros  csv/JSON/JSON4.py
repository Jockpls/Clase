import json

try:
    with open('datoscorrupt.json', 'r') as usuarios:
        usuarios = json.load(usuarios)

except json.decoder.JSONDecodeError:
    print('El archivo está corrupto')