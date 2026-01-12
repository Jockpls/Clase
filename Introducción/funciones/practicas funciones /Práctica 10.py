def promedio_alumno(notas):
    promedio = (sum(notas) / len(notas))
    print(f"El promedio del alumno es: {promedio:.2}")

def aprobaron(lista_notas):
        for i in lista_notas:
            if i >= 5:
                print(f"El alumno aprueba con un {i}")
            else:
                print(f"El alumno suspende con un {i}")

def main():
    notas = [9,6,2,4,3,7,4,10,10]
    promedio_alumno(notas)
    lista_notas = [6,9,7,1,2,4,3,5,6]
    aprobaron(lista_notas)
main()