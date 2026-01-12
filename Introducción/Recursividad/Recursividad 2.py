def suma_n(n):
    if n == 1:
        return 1
    else:
        return n + suma_n(n-1)

def main():
    n = int(input("Dame un número: "))
    print(suma_n(n))

main()