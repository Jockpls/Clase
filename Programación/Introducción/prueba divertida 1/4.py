dni = input("Introduce tu DNI(8 número y 1 letra): ")
i = int(dni[0:8])
letra = dni[8]
calculoletra = i%23
lista = ["T","R","W","A","G","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
if letra == lista[calculoletra]:
    print("La letra del DNI es correcta")
else:
    print(F"la letra es incorrecta {lista[calculoletra]}")