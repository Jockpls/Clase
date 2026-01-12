def extremos(lista):
        minimo = min(lista)
        maximo = max(lista)
        return minimo,maximo


def main():
    lista = ["6", "1", "0", "9", "4", "9"]
    extremos(lista)
    resultados = extremos(lista)
    print(resultados)

main()
