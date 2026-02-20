class libro():

    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"El título es {self.titulo}, el autor es {self.autor}, y se publicó en el año {self.año}"

    def __repr__(self):
        return f"libro({self.titulo}, {self.autor}, {self.año})"

def main():
    libro1 = libro("Jarry petas", "JK Rowling", "1992")
    print(libro1)
    print(repr(libro1))
main()