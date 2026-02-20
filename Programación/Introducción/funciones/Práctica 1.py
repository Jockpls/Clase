lista = ["1","2","3","4","5","6"]
def contar_pares(lista):
    contador = 0
    for i in range(len(lista)):
        if i%2 == 0:
            contador += 1
    print(f"La cantidad de números pares es {contador}")


contar_pares(lista)