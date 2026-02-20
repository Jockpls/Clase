while True:
    palindromo1 = input("Introduce una palabra para ver si es un palindromo: ")
    palininvert1 = palindromo1[::-1]
    if palindromo1 == palininvert1:
        print(f"{palindromo1} se lee igual para alante que para atrás")
        break
    elif palindromo1 != palininvert1:
        print("Intentalo de nuevo.")