try:
    edad = int(input("Introduce tu edad: "))
    print("Edad registrada:", edad)
except ValueError:
    print("Edad no válida")
finally:
    print("Registro finalizado")

'''
El codigo hace una comprobación de errores a la hora de registrar un usuario en una base, de manera que este
no pueda introducir valores incorrectos y no se corrompa la integridad de los datos de la BBDD.
Primero, pide que se introduzca un valor numérico entero para la edad, devolviendo un error de valor al no ser correcto
y "terminando" en el finally con el registro.
'''