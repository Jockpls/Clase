class Alumno():
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.asignaturas = []

    def add_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def listar_asignaturas(self):
        return self.asignaturas



class Asignatura():
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def add_nota(self, nota):
        self.notas.append(nota)

    def __str__(self):
        return f"{self.nombre} - {self.notas}"

    def media_nota(self):
        return sum(self.notas) / len(self.notas)

def main():
    alumno = Alumno("Felix", 1)
    asignatura = Asignatura("Programacion")
    alumno.add_asignatura()



main()

notas = {}

asignatura = input("Asignatura: ")
nota = int(input("Nota: "))

notas[asignatura] = nota

print(notas)
notas["lengua"] = 10

print(notas)
notas["lengua"] = 8

print(notas)

