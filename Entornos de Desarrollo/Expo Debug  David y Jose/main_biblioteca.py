from biblioteca import Biblioteca
from libro import Libro

def main():
    bib = Biblioteca()
    libro1 = Libro("123-4-56-78901-2", "Python 101", "Ana Pérez", 3)
    bib.registrar_libro(libro1)

    # Préstamos
    bib.prestar_libro("123-4-56-78901-2")
    bib.prestar_libro("123-4-56-78901-2")
    bib.prestar_libro("123-4-56-78901-2")   # última copia

    # Intentar otro préstamo (debe fallar)
    try:
        bib.prestar_libro(" ")
    except RuntimeError as e:
        print(e)
    except KeyError as e:
        print(e)

    # Devolución
    bib.devolver_libro("123-4-56-78901-2")
    print(f"Copias disponibles: {libro1.copias}")

if __name__ == "__main__":
    main()
