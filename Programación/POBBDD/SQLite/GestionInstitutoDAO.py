"""
1 Crear clases Alumno, Asignatura y Matricula.
6 Hacer consultas con JOIN.
7 Actualizar datos.
8 Eliminar datos
"""

import sqlite3


class Alumno:
    def __init__(self, nombre, edad, id=None):
        self.nombre = nombre
        self.edad = edad
        self.id = id


class Asignatura:
    def __init__(self, nombre, horas, id=None):
        self.nombre = nombre
        self.horas = horas
        self.id = id


class matricula:
    def __init__(self, nota, id=None, alumno_id=None, asignatura_id=None):
        self.nota = nota
        self.id = id
        self.alumno_id = alumno_id
        self.asignatura_id = asignatura_id


class InstitutoDAO:
    def __init__(self, highschool_bd):
        self.highschool_bd = highschool_bd

    def _conectar(self):
        return sqlite3.connect("self.highschool_db")

    def crear_alumno(self, alumno):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER,
        """
        )

        conectar.commit()
        conectar.close()

    def crear_asignatura(self, asignatura):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS asignaturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        horas INTEGER,
        """
        )

        conectar.commit()
        conectar.close()

    def crear_matricula(self):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS matriculas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nota FLOAT,
        alumno_id INTEGER,
        asignatura_id INTEGER,
        CONSTRAINT FOREIGN KEY(alumno_id) REFERENCES alumnos(id)
        CONSTRAINT FOREIGN KEY(asignatura_id) REFERENCES asignaturas(id)
        """
        )

        conectar.commit()
        conectar.close()

    def insertar_alumno(self, alumno):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "INSERT INTO alumnos(id, nombre, edad) VALUES (?,?,?)",
            (alumno.id, alumno.nombre, alumno.edad),
        )

        conectar.commit()
        conectar.close()

    def insertar_Asignatura(self, asignatura):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "INSERT INTO asignaturas(id, nombre, horas) VALUES (?,?,?)",
            (asignatura.id, asignatura.nombre, asignatura.horas),
        )

        conectar.commit()
        conectar.close()

    def insertar_matricula(self, matricula, alumno, asignatura):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute(
            "INSERT INTO matriculas(id, nota, alumno_id, asignatura_id) VALUES (?,?,?,?)",
            (matricula.id, matricula.nota, alumno.id, asignatura.id),
        )

        conectar.commit()
        conectar.close()

    def obtener_alumnos(self, alumno):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute("SELECT * FROM alumnos")

        filas = cursor.fetchall()
        conectar.close()

        alumnos = []

        for fila in filas:
            alumnos.append(Alumno(fila[0], fila[1], fila[2]))

    def obtener_asignaturas(self, asignatura):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute("SELECT * FROM asignaturas")
        filas = cursor.fetchall()
        conectar.close()

        asignaturas = []

        for fila in filas:
            asignaturas.append(Asignatura(fila[0], fila[1], fila[2]))

    def obtener_matriculas(self, matricula):
        conectar = self._conectar()
        cursor = conectar.cursor()

        cursor.execute("SELECT * FROM matriculas")

        filas = cursor.fetchall()
        conectar.close()

        matriculas = []

        for fila in filas:
            matriculas.append(matricula(fila[0], fila[1], fila[2], fila[3]))
