from libro import Libro

class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def registrar_libro(self, libro: Libro):

        self.catalogo[libro.isbn] = libro

    def prestar_libro(self, isbn: str):
        libro = self.catalogo.get(isbn)
        if libro is None:
            raise KeyError("Libro no encontrado")
        if not libro.disponible():

            raise RuntimeError("No hay copias disponibles")
        libro.prestar()

    def devolver_libro(self, isbn: str):
        libro = self.catalogo.get(isbn)
        if libro is None:
            raise KeyError("Libro no encontrado")
        libro.devolver()
