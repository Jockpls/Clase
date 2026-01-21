try:
    data = open('datos.txt', 'rt')
    datillos = data.readlines()
    print(datillos)
    data.close()
except FileNotFoundError:
    print('El fichero no existe')