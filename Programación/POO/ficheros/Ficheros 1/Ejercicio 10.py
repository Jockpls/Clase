try:
    with open('logs.txt', 'wt') as log:
        mensaje = input('Introduzca algo: ')
        while mensaje != 'exit':
            mensaje = input('Introduzca algo: ')
            log.write(mensaje)
    log.close()
except PermissionError:
    print('Access Denied')
except IOError:
    print('Ha ocurrido un fallo, yokse hermano.')
