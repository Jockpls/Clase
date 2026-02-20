class animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
       print("")

class dog(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        return f"{self.nombre} dice miau miau porque es dislexico"


class cat(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        print(f"{self.nombre} dice miau miau madafaka")

def main():
    firulais = dog(nombre = "firulais")
    print(firulais.hablar())
    misifú = cat(nombre = "misifú")
    misifú.hablar()


main()