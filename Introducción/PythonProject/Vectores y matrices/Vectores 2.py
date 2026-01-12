print("Quiero que me des una lista de números para hacer una suma y calcular el promedio, pulsa enter para salir")
lista = []
n2 = 0
while True:
    n = input("Dame un número entero para la lista: ")
    if n != "":
        n = int(n)
        lista.append(n)
        n2 += n
        print(lista)
        print(n2)
    else:
        break
promedio = n2/len(lista)
print(f"Tu lista es esta {lista}, la suma es {n2} y el promedio es {promedio:.2f}")