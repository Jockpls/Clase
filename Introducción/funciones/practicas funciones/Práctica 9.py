def calculo_matriz(matriz, operacion, numero):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(n):
        for j in range(m):
            match operacion:
                case "+":
                    matriz[i][j] += numero
                case "-":
                    matriz[i][j] -= numero
                case "*":
                    matriz[i][j] *= numero
                case "/":
                    matriz[i][j] /= numero
                case _:
                    print("none")

def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    numero = int(input("Dame un número para operar: "))
    calculo_matriz(matriz, "+", numero)
    print(matriz)
    calculo_matriz(matriz, "-", numero)
    print(matriz)
    calculo_matriz(matriz, "*", numero)
    print(matriz)
    calculo_matriz(matriz, "/", numero)
    print(matriz)
main()