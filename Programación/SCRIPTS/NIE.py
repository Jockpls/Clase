#Programa para calcular la letra del NIE y del DNI

def documento(documento):
#Primero declaramos variables y el diccionario a utilizar.
    data_nie = str.maketrans("XYZ","012")

    while True:
        documento = input("Introduce tu DNI o NIE: ")
        documentomayus = documento.upper()
        if len(documentomayus) == 9:
            if documentomayus[1:8].isdigit() == False:
                print("Documento mal introducido")
            elif documentomayus[8].isalpha() == False:
                print("Documento mal introducido, el último caracter no es una letra")
            elif documentomayus[0].isdigit() == False and documentomayus[0] != "X" and documentomayus[0] != "Y" and documentomayus[0] != "Z":
                print("Documento mal introducido")
            else:
                for i in range(1):
                    i = documentomayus[0:8].translate(data_nie)

                dni_letra = documentomayus[8]
                dni = int(i)    ##Convertimos la letra del NIE en un número

                # Esta es la operación para ver si el documento se ha introducido bien.
                calculoletra = dni % 23
                lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L",
                         "C", "K", "E"]
                if dni_letra == lista[calculoletra]:
                        print("La letra del documento es correcta")
                        break
                else:
                        print(f"la letra del documento es incorrecta debería ser {lista[calculoletra]}")
                break
        else:
            print("El documento tiene que tener 9 caracteres")