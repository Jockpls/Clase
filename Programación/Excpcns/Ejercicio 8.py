try:
    user = input("Introduzca su usuario: ")
    pasw = input("Introduzca su password: ")
    if len(pasw) < 8:
        raise ValueError

except ValueError:
    print('Longitud de contraseña incorrecta')
else:
    print("Usuario registado.")
finally:
    print("¿Qué mayonesa te gusta más?")