class Alumno():                                     #Crea clase alumno
   def __init__(self, nombre):
       self.nombre = nombre

class Curso():                                      #Crea clase curso
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso            #Definimos qué curso es
        self.alumnos = []                           #Es la lista de alumnos que tenemos

    def agregar_alumno(self, alumno):               #Creo el metodo para hacer la lista de alumnos, con la clase entera
        self.alumnos.append(alumno)

    def listar_alumnos(self):                       #Creo el metodo para obtener la lista de alumnos
        return self.alumnos

def main():
    curso = Curso("1ºDawB")
    al1 = Alumno("Jose Carlos")
    al2 = Alumno("Naiara")

    curso.agregar_alumno(al1)                       #Introducimos a los alumnos en la lista(en curso)
    curso.agregar_alumno(al2)

    alumnos = curso.listar_alumnos()                #Definimos la lista para recorrerla

    for alumno in alumnos:
        print(f"El nombre del alumno es {alumno.nombre}")

main()