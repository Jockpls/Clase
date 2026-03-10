class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, copias: int):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def prestar(self):
        self.copias -= 1

    def devolver(self):
        self.copias += 1

    def disponible(self):
        return self.copias > 0
