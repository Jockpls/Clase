try:
    num = int(input("Introduce un numero entero positivo: "))
    if num < 0:
        raise ValueError("El numero debe ser positivo")
    if num > 100:
        raise ValueError("El numero no debe ser mayor que 100")
except ValueError as e:
    print("Error:", e)
else:
    print(num**2)
finally:
    print("Mayonesa pasillo 5")

