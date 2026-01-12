#Programa para pedir una lista de palabras, preguntar por palabras, ver si está en la lista y qué posición tiene

lista = []
n = 0
while True:
    n = input("Dame una palabra para la lista: ")
    if n != "":
        lista.append(n)
        print(lista)
    else:
        print("Ok, es suficiente")
        break
while True: #bucle para ver si la palabra está en la lista
    i = input("Veamos si la palabra está en la lista: ")
    if i in lista:
        print(f"Correcto, {i} está en la lista y su posición es {lista.index(i)}")
        i = input("Dame otra palabra para ver su posición, pulsa intro para terminar: ")
    elif i == "":
        print("Gracias por su tiempo")
        break
    else:
       print(f"{i} no está en la lista, intentalo de nuevo.")
