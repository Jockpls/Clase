print("Quiero una lista de números, pulsa enter para terminar")

n = 0
lista = []

while True:
    n = input("Introduce un número: ")
    if n != "":
        n = int(n)
        lista.append(n)
    elif n == "":
        break
print(f"Esta es tu lista {lista}")

maximo = lista[0]
minimo = lista[0]

for i in range(len(lista)):
    if lista[i] < minimo:
        minimo = lista[i]
    elif lista[i] > maximo:
        maximo = lista[i]

print(f"El valor máximo es {maximo} y el minimo es {minimo}.")