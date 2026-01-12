class Alumno:

    def __init__(self, nombre: str, dni: str):
        self.nombre = nombre
        self.__dni = "00000000X"
        self.__calificaciones = {}
        self.dni = dni

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if dni == dni[0:8] and dni[8].isalpha():
            dni[8].upper()
            self.__dni = dni

    @property
    def calificaciones(self):
        return self.__calificaciones

    def establecer_calificacion(self, modulo: str, nota: float):
        if nota >= 0 and nota <= 10:
            self.__calificaciones[modulo] = nota
            return True
        else:
            return False

    def __str__(self):
        return f"{self.nombre} asignatura{self.calificaciones}"

class Curso:

    def __init__(self, nombre_curso: str, codigo: str):
        self.nombre_curso = nombre_curso
        self.__codigo = codigo
        self.__alumnos = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def alumnos(self):
        return self.__alumnos

    def inscribir_alumno(self, alumno):
        for alu in self.__alumnos:
            if alu.dni == alumno.dni:
                return f"El alumno ya fue agregado"

        self.__alumnos.append(alumno)
        return f"El alumno ha sido inscrito"

    def obtener_alumno(self, dni):
        for alumno in self.__alumnos:
            if dni == alumno.dni:
                return None
            else:
                return dni

    def calcular_media_curso(self, modulo):
        suma_notas = 0
        numero_notas = 0
        for alumno in self.__alumnos:
            if modulo in alumno.calificaciones[modulo]:
                numero_notas += 1
                suma_notas += Alumno.calificaciones[modulo]
            else:
                None
            return suma_notas/numero_notas

    def listar_alumnos(self):
        return self.__alumnos

def menu(curso) :
    # Creamos el menú
    while True:
        print("1. Listar alumnos inscritos")
        print("2. Inscribir nuevo alumno (nombre y DNI)")
        print("3. Asignar o modificar calificación (pide DNI del alumno, módulo y nota)")
        print("4. Calcular media de un módulo para todo el curso (pide nombre del módulo")
        print("5. Salir")
        menu = int(input("Elige una opción: "))
        match menu:
            case 1:
                alumnos = curso.listar_alumnos()
                for alumno in alumnos:
                    print(alumno)
            case 2:
                name= input("Introduce el nombre: ")
                dni = input("Introduce el DNI: ")
                curso.obtener_alumno(name, dni)
            case 3:
                Alumno.establecer_calificacion()
            case 4:
                curso.calcular_media_curso()
            case 5:
                break
            case _:
                print("Tienes que seleccionar una de las opciones disponibles")

def inicializar_curso() -> Curso:
    #Creamos el curso
    curso = Curso("Desarrollo de Aplicaciones Web", "DAW-2025")
    print(f"\n--- INICIALIZANDO CURSO: {curso.nombre_curso} ---")

    #Añadimos los alumnos
    a1 = Alumno("Marta Ríos", "50123456T")
    a2 = Alumno("Javier Salas", "71987654Z")

    #Añadimos uno mal de prueba
    a3 = Alumno("Lucas Pérez", "123456789")
    print(f"DNI de Lucas Pérez tras intento fallido: {a3.dni}")

    #Inscribimos los alumnos
    print(curso.inscribir_alumno(a1))
    print(curso.inscribir_alumno(a2))
    print(curso.inscribir_alumno(a3))

    #Introducimos las calificaciones
    a1.establecer_calificacion("Programacion", 7.5)
    a1.establecer_calificacion("BBDD", 8.0)
    a2.establecer_calificacion("Programacion", 5.0)
    a2.establecer_calificacion("BBDD", 9.5)

    print("--------------------------------")
    return curso

if __name__ == '__main__':
    academia = inicializar_curso()
    menu(academia)