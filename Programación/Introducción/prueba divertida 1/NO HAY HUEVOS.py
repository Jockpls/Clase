lista = ["T","R","W","A","G","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

documento = input("Introduce tu DNI o NIE: ")

letra_dni = documento[8].upper()
numero_dni = int(documento[1:8])
while True:
    letranie = documento[0].upper()
    if letranie == "X":
        X = 0
        break
    elif letranie == "Y":
        Y = 1
        break

