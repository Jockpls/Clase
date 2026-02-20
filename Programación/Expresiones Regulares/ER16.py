"""Crea un programa que valide un formulario con:
- Nombre (solo letras y espacios)
- Email
- Teléfono
- Código postal
- Contraseña segura
Debe indicar qué campos son válidos y cuáles no."""
import re
class ParametroError(Exception):
    pass

Nombre = input("Ingrese su nombre: ")
Email = input("Ingrese su email: ")
Tel = input("Ingrese su telefono: ")
cp = input("Ingrese su Código Postal: ")
Password = input("Ingrese su contraseña: ")

try:
    if not re.fullmatch(r"[A-ZÁÉÍÓÚ]?[a-záéíóú]*\s?[A-ZÁÉÍÓÚ]?[a-záéíóú]*", Nombre):
        raise ParametroError('Nombre inválido')
    if not re.fullmatch(r"[A-Za-z0-9\S]+@[A-Za-z]+\.[a-z]{2,4}$", Email):
        raise ParametroError(f'Email no válido')
    if not re.fullmatch(r"6[0-9]{8}|7[0-9]{8}|9[0-9]{8}", Tel):
        raise ParametroError('Teléfono no válido')
    if not re.fullmatch('[0-9]{5}', cp):
        raise ParametroError('Código Postal no válido')
    if not re.fullmatch(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w])[^\s]{8,}$", Password):
        raise ParametroError('Contraseña no válida')
except ParametroError as e:
    print(e)
else:
    print('Usuario creado correctamente')
finally:
    print('Besitos en el pito')