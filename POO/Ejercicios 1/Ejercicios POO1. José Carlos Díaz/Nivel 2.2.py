class alumno:

    def __init__(self, nota):
        self.__nota = nota  #Con la variable nota defino "__nota"

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):   #Al añadir el argumento "nota", la variable que yo defina en el main será la que obtenga cómo parámetro.
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota Incorrecta.")
        else:
            self.__nota = nota      #Aquí ya se cambia el atributo en el objeto


def main():
    nota = int(input("Introduce una nota: "))
    Joseca = alumno(nota)
    print(f"La nota del alumno es: {Joseca.nota}")
    Joseca.nota = 10
    print(f"La nota del alumno es: {Joseca.nota}")

main()