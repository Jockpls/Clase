"""
MEJORAS

Se cambia el sistema de ifs por match/case
Se suprimen espacios innecesarios
Se suprimen booleanos innecesarios
Se amplia el print del caso 4 para mostrar más datos
caso 5:
    - La variable total pasa a llamarse total_peliculas para identificar mejor la variable
    - La suma se simplifica
    - Se ordena y unifica el bucle, evitando tener bucles de mas, y entendiendo mejor por partes el output que nos devuelve
"""

peliculas = [
    ["Matrix", "SciFi", 1999, 3],
    ["Titanic", "Drama", 1997, 2],
    ["Toy Story", "Animacion", 1995, 5],
]

alquileres = []

def menu():
    print()
    print("1 Ver peliculas")
    print("2 Alquilar pelicula")
    print("3 Devolver pelicula")
    print("4 Buscar por genero")
    print("5 Estadisticas")
    print("6 Salir")

while True:
    menu()
    op = input("Opcion: ")
    match op:
        case '1': #Ver peliculas
            for p in peliculas:
                print("Titulo:", p[0])
                print("Genero:", p[1])
                print("Año:", p[2])
                print("Disponibles:", p[3])
                print("----------------")

        case "2": #Alquilar película
            titulo = input("Titulo: ")
            usuario = input("Usuario: ")
            for p in peliculas:
                if p[0].lower() == titulo.lower():
                    if p[3] > 0:
                        p[3] = p[3] - 1
                        alquileres.append([titulo, usuario])
                        print("Alquiler realizado")
                    else:
                        print("No hay copias disponibles")
                    break
            else:
                print("Pelicula no encontrada")

        case "3":
            titulo = input("Titulo: ")
            usuario = input("Usuario: ")
            for a in alquileres:
                if a[0].lower() == titulo.lower() and a[1] == usuario:
                    alquileres.remove(a)
                    for p in peliculas:
                        if p[0].lower() == titulo.lower():
                            p[3] = p[3] + 1
                    print("Pelicula devuelta")
                else:
                    print("No existe ese alquiler")

        case "4":
            genero = input("Genero: ")
            for p in peliculas:
                if p[1].lower() == genero.lower():
                    print(f'Nombre: {p[0]}, Año: {p[2]}, Disponibles: {p[3]}')

        case "5":
            total_peliculas = 0
            generos = {}
            
            for p in peliculas:
                total_peliculas += p[3]
                print("Copias disponibles:", total_peliculas)
                print("Peliculas alquiladas:", len(alquileres))
                genre = p[1]
                if genre not in generos:
                    generos[genre] = 1
                else:
                    generos[genre] = generos[genre] + 1

            print("Peliculas por genero:")
            for genre in generos:
                print(genre, generos[genre])

        case "6":
            break
        case _:
            print("Opcion incorrecta")