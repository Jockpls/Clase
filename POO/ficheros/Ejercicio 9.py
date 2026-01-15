fichero = input('Introduce el nombre de un fichero: ')
try:
    file = open(fichero, 'r')
    lector = file.read()
    print(lector)
    file.close()

except FileNotFoundError:
    print('El fichero no existe')
except PermissionError:
    print('Permiso denegado')