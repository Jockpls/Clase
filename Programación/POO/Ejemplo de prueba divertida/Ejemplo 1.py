#Creo clase alumno
class Alumno():
    def __init__(self, nombre: str, dni: str):
        self.nombre = nombre
        self.__calificaciones = {}  #{modulo: nota}
        self.__dni = "00000000X"
        #El constructor llama al setter para validar el DNI inicial
        self.dni = dni

    @property                       #DNI Como propiedad
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):              #En el setter hacemos prueba de errores
        if len(dni) == 9:
            if dni[0:8].isdigit() == True and dni[8].isalpha() == True:
                self.__dni = dni

    @property                       #calificaciones como propiedad
    def calificaciones(self):
        return self.__calificaciones

    def establecer_calificacion(self, modulo: str, nota: float):
        self.__calificaciones[modulo] = nota

    def __str__(self):
        return f"El alumno {self.nombre} con el dni {self.dni} sus calificaciones son {self.calificaciones}."

class Curso:
    def __init__(self, nombre_curso: str, codigo: str):
        self.nombre_curso = nombre_curso
        self.__codigo = codigo
        self.__alumnos = []

    @property
    def alumnos(self):
        return self.__alumnos

    @property
    def codigo(self):
        return self.__codigo

    def inscribir_alumno(self, alumno):
        for alu in self.__alumnos:
            if alu.dni == alumno.dni:
                return f"Ya está inscrito"

        self.__alumnos.append(alumno)
        return f'El alumno ha sido inscrito'


    def obtener_alumno(self, dni):
        for alumno in self.__alumnos:
            if alumno.dni == dni:
                return alumno

        return False

    def calcular_media_curso(self, modulo: str):
        suma_notas = 0
        cantidad_notas = 0
        for alumno in self.__alumnos:
            if modulo in alumno.calificaciones:
                suma_notas += alumno.calificaciones[modulo]
                cantidad_notas += 1
                print(cantidad_notas)
        media = suma_notas/cantidad_notas
        return float(media)


    def listar_alumnos(self):
        return self.__alumnos

def menu(curso):
    while True:
        print(f"1. Listar alumnos inscritos.")
        print(f"2. Inscribir nuevo alumno.")
        print("3. Asignar o modificar una calificación.")
        print("4. Calcular la media del módulo para un curso.")
        print("5. Salir.")
        menu = int(input("¿Qué quieres hacer? "))
        match menu:
            case 1:
                alumnos = curso.listar_alumnos()
                for alumno in alumnos:
                    print(alumno)
            case 2:
                name = input("Dame el nombre del nuevo alumno. ")
                dni = input("Introduce el dni del alumno")
                nuevo_alumno = Alumno(name, dni)
                curso.inscribir_alumno(nuevo_alumno)
            case 3:
                dni = input("Introduce el DNI del alumno. ")
                alumno = curso.obtener_alumno(dni)
                if alumno:
                    modulo = input("Introduce el modulo a calificar: ")
                    nota = float(input("Introduce la nota del modulo: "))
                    alumno.establecer_calificacion(modulo, nota)
                else:
                    print("Ese alumno no existe.")

            case 4:
                mod = input("¿De qué modulo quieres hacer la media? ")
                print("La media es:", curso.calcular_media_curso(mod))
            case 5:
                break
            case _:
                print("Entrada incorrecta, inténtelo de nuevo.")
    # = BLOQUE DE PRUEBA (main function) =
def inicializar_curso() -> Curso:
    """Función para pre-cargar el curso con datos para la prueba."""

    """Al comentar con almoadilla solo se comenta esa linea 
    mientras que con las comillas se comenta todo lo que esté entre ellas."""

    #creamos el curso
    curso = Curso("Desarrollo de Aplicaciones Web","DAW-2025")
    print(f"\n--- INICIALIZANDO CURSO: {curso.nombre_curso} ---")

    #Alumnos válidos
    a1 = Alumno("Marta Ríos", "50123345T")
    a2 = Alumno("Javier Salas", "71987654Z")

    #Alumno con DNI inválido
    a3 = Alumno("Lucas Pérez", "123456789")
    print(f"DNI de {a3.nombre} tras intento fallido: {a3.dni}") #Mostrará 00000000X

    #Inscripciones
    print(curso.inscribir_alumno(a1))
    print(curso.inscribir_alumno(a2))
    print(curso.inscribir_alumno(a3))   #Se inscribe aunque tenga el DNI por defecto

    #Calificaciones
    a1.establecer_calificacion("Programación", 7.5)
    a1.establecer_calificacion("BBDD", 8.0)
    a2.establecer_calificacion("Programación", 5.0)
    a2.establecer_calificacion("BBDD", 9.5)

    print("----------------------")
    return curso

if __name__ == "__main__":
    academia = inicializar_curso()
    menu(academia)

