def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("¿Cuántos números de fibonacci quieres realizar?: "))
    print(fibonacci(n))

main()