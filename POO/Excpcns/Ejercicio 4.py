usuarios = {
    "ana": 23,
    "luis": 30,
    "maria": 19
}
try:
    user = input("Ingrese nombre del usuario: ")
    print(f'{user} tiene {usuarios[user]} años.')
except KeyError:
    print("Usuario no encontrado")