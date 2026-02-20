suma_notas = 0
lista_notas = []
contador = 0
for i in range(0,5):
    contador += 1
    nota = int(input(f"Introduce la nota del alumno {contador}: "))
    suma_notas += nota
    lista_notas.append(nota)
print(lista_notas)
print(f"El promedio de las notas es: {suma_notas/len(lista_notas)}")
promedio = suma_notas/len(lista_notas)

for i in range(0,5):
    if promedio < lista_notas[i]:
        print(f"El alumno {i+1} tiene un {lista_notas[i]} encima de la media por {i - promedio}")
    elif promedio > lista_notas[i]:
        print(f"El alumno {i+1} tiene un {lista_notas[i]} debajo de la media por {promedio-i}")
    elif promedio == lista_notas[i]:
        print(f"El alumno {i+1} tiene un {lista_notas[i]}, está en la media")
