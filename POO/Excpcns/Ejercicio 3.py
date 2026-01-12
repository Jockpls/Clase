nombres = ["Ana", "Luis", "Maria", "Carlos"]
try:
    position = int(input('¿Qué posición de la lista quiere saber? '))
    print(nombres[position-1])
except ValueError:
    print("Error, valor incorrecto")
except IndexError:
    print("Error, indice no encontrado")