class Gato:

    def __init__(self, nombre, dueño):
        self.nombre = nombre
        self.dueño = dueño

    def get_nombre(self):
        return self.nombre

    def maullido(self):
        print(f"{self.nombre} miauuu!! a {self.dueño}")


def main():
    niebla = Gato("Niebla", "Joseca")
    niebla.maullido()

main()