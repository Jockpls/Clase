def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = int(input("Dame un numero para ver su factorial: "))
    print(factorial(n))


main()