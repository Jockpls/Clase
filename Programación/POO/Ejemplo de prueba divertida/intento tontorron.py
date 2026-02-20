class Alumno():

    def __init__(self, nombre: str, dni: str):
        self.nombre = nombre
        self.__dni = "00000000X"
        self.__calificaciones = {}
        #El constructor llama al setter para validar el dni inicial
        self.dni=dni
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):  # En el setter hacemos prueba de errores
        if len(dni) == 9:
            if dni[0:8].isdigit() == True and dni[8].isalpha() == True:
                self.__dni = dni

    @property
    def calificaciones(self):
        return self.__calificaciones

    def establecer_calificacion(self, modulo: str, nota: float):
        self.__calificaciones[modulo] = nota
        if nota <= 10 and nota >= 0:
            return True
        else:
            return False
    def __str__(self):
        return f'{self.nombre} con DNI {self.dni} ha obtenido las siguientes calificaciones {self.__calificaciones}.'

class Curso():
    def __init__(self, nombre_curso: str, codigo: str):
        self.nombre_curso = nombre_curso
        self.__codigo = codigo
        self.__alumnos = []

    @property
    def alumnos(self):
        return self.__alumnos

    @property
    def codigo(selfs):
        return self.__codigo

    def inscribir_alumno(self, alumno):
        for alu in self.__alumnos:
            if alu.dni == alumno.dni:
                return f'El alumno ya existia.'
        self.__alumnos.append(alumno)
        return f'El alumno ha sido inscrito.'

    def obtener_alumno(self, dni):
        for alumno in self.__alumnos:
            if alumno.dni == dni:
                return alumno

        return False

    def calcular_media_curso(self, modulo)  ->float:
        contador = 0
        sumador = 0
        for alumno in self.__alumnos:
            if modulo in alumno.calificaciones:
                sumador += alumno.calificaciones[modulo]
                contador += 1
        media = sumador/contador
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
        menu = int(input(f'¿Qué quieres hacer? '))
        match menu:
            case 1:
                alumnos = curso.listar_alumnos()
                for alumno in alumnos:
                    print(alumno)
            case 2:
                name = input('Introduce el nombre del alumno. ')
                Dni = input(f'Introduce el DNI del alumno. ')
                alumno = Alumno(name,Dni)
                print(curso.inscribir_alumno(alumno))
            case 3:
                dni = input(f'Introduce el DNI del alumno. ')
                alumno = curso.obtener_alumno(dni)
                if alumno:
                    modulo = input(f'¿A qué modulo quieres añadir la nota?')
                    nota = float(input(f'¿Cuál es la calificación del alumno? '))
                    alumno.establecer_calificacion(modulo, nota)
                else:
                    print(f'Ese alumno no existe.')
            case 4:
                modulo = input(f'¿Para qué modulo quieres calcular la nota? ')
                print(curso.calcular_media_curso(modulo))
            case 5:
                break
            case _:
                print(f'Entrada incorrecta, inténtelo de nuevo.')

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

