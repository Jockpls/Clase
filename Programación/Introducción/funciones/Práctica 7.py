def matriz_identidad(n):
    matriz_resultado = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matriz_resultado[i][j] = 1
    return matriz_resultado

def matriz_identidad2(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def main():
    n = int(input("Dime la identidad de tu matriz: "))
    matriz = matriz_identidad(n)
    print(matriz)
    matriz2 = matriz_identidad2(n)
    print(matriz2)
main()

