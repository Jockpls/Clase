def validar_precio(precio):
    if precio < 0:
        raise ValueError

try:
    precio = float(input("¿Cuál es el precio? "))
    validar_precio(precio)
except ValueError:
    print("El valor no puede ser negativo.")
else:
    print(precio)
finally:
    print("Hellmanns, la mayonesa de los mayoneseros.")
