import sqlite3

"""
Práctica: Gestión de Alumnos con DAO en Python
Desarrolla una aplicación en Python que permita gestionar una base de datos de alumnos usando
SQLite, POO y el patrón DAO.
Base de datos: instituto.db. Tabla: alumnos (id, nombre, edad, curso).
Crea una clase Alumno con atributos id, nombre, edad y curso, y método __str__.
Crea una clase AlumnoDAO con los métodos: crear_tabla(), insertar(), obtener_todos(),
buscar_por_nombre(), actualizar_curso(), eliminar().
Programa de prueba: insertar alumnos, mostrar, buscar, actualizar y eliminar.
Reflexiona: ¿Por qué usar id? ¿Qué ventajas tiene DAO?
"""

class Alumno:
    def __init__(self, id, nombre, edad, curso):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.edad}, {self.curso}'

class AlumnoDAO:
    def __init__(self, instituto_bd):
        self.instituto_bd = instituto_bd

    def _conectar(self):
        return sqlite3.connect(self.instituto_bd)

    def crear_tabla(self):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            curso TEXT NOT NULL)              
            """)

        conectar.commit()
        conectar.close()

    def insertar(self, alumno):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "INSERT INTO alumnos (id, nombre, edad, curso) VALUES (?, ?, ?, ?)",
            (alumno.id, alumno.nombre, alumno.edad, alumno.curso)
        )

        conectar.commit()
        conectar.close()

    def obtener_todos(self):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "SELECT id, nombre, edad, curso FROM alumno"
        )

        filas = cursor.fetchall()
        conectar.close()

        alumnos = []

        for fila in filas:
            alumnos.append(Alumno(fila[0], fila[1], fila[2], fila[3]))

        return alumnos

    def buscar_por_nombre(self, texto):

        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "SELECT nombre FROM alumnos WHERE nombre LIKE ?",
            ("%"+texto+"%",)
        )

        filas = cursor.fetchall()
        conectar.close()

        alumnos = []

        for fila in filas:
            alumnos.append(Alumno(fila[0], fila[1], fila[2], fila[3]))

        return alumnos

    def actualizar_curso(self, edad, curso, id):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "UPDATE alumnos SET edad = ?, curso = ? WHERE id = ?",
            (id, edad, curso)
        )

        conectar.commit()

        filas = cursor.rowcount

        conectar.close()

        return filas

    def eliminar(self, id):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "DELETE FROM alumnos WHERE id = ?",
            (id,)
        )

        conectar.commit()
        filas = cursor.rowcount
        conectar.close()

        return filas

def main():
    dao = AlumnoDAO("clase.db")

    dao.crear_tabla()

    dao.insertar(Alumno(1, "Jose Carlos", 29, '1DAW'))
    dao.insertar(Alumno(2, "Paco", 18, '1DAW'))
    dao.insertar(Alumno(3, "Pedro", 22, '1DAW'))
    dao.insertar(Alumno(4, "David", 20, '1DAW'))
    dao.insertar(Alumno(5, "Eva", 20, '1DAM'))

    print("Alumnos admitidos.")

    alumnos = dao.obtener_todos()

    for alumno in alumnos:
        print(alumno)

    dao.eliminar(3)

    dao.actualizar_curso(4)


main()