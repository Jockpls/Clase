# =====================================================
# EXAMEN 1º DAW - PROGRAMACION (PYTHON)
# Archivo entregado a José Carlos: contiene ERRORES
# =====================================================
import re
import os

class ArchivoNoEncontradoError(Exception):
    pass
class EmailError(Exception):
    pass

class Persona:
    def __init__(self, nombre: str, email: str, telefono: int): #Definimos los tipos de datos y añado los dos puntos al final del constructor
            self.telefono = telefono
            if not validar_email(email):
                self.email = email
            else:
                self.email = email
            self.nombre = nombre

    def resumen(self):  #Añado el self al metodo
        return f"{self.nombre} - {self.email} - {self.telefono}"


class Alumno(Persona):
    def __init__(self, nombre, email, telefono, grupo: str, notas: list): #Corrijo los tipos de datos
        super().__init__(nombre, email, telefono) #Se corrige la llamada a la funcion super con los dos parentesis
        self.grupo = grupo
        self.notas = notas  #Buen intento Antonio

    def media(self, notas):
        total = sum(self.notas) / len(self.notas)
        return total

    def add_nota(self, nota): #Añado los dos puntos
        self.notas.append(float(nota))    #Cambio el tipo de dato de entero a float

    def resumen(self):  #Añado el self al metodo
        return f"{self.nombre} - {self.email} - {self.telefono} - {self.grupo} - media = {self.media(self.notas)}"

class Profesor(Persona):
    def __init__(self, nombre, email, telefono, departamento, salario):
        super().__init__(nombre, email, telefono)
        self.departamento = departamento
        self.salario = float(salario)

    def aplicar_subida(self, porcentaje):
        self.salario = self.salario + self.salario * porcentaje / 100

    def resumen(self):
        base = Persona.resumen()
        return base + f" - {self.departamento} - {self.salario} - {self.departamento} - {self.salario}"

def parsear_notas(notas):
    if notas == "": #Faltan los dos puntos
        return []

    trozos = notas.split("|")
    return [float(x) for x in trozos] #Me gustan más las notas cómo float


def crear_persona_desde_campos(campos):
    try:
        tipo = campos[0].strip()
        if tipo == "A": #Otros dos puntos
            nombre = campos[1]
            email = campos[2]
            telefono = campos[3]
            grupo = campos[4]
            notas = parsear_notas(campos[5])
            return Alumno(nombre, email, telefono, grupo, notas) #El objeto se compone de 5 campos, no 6, elimino "Extras"
        elif tipo == "P":
            nombre = campos[1]
            email = campos[2]
            telefono = campos[3]
            departamento = campos[4]
            salario = campos[5]
            return Profesor(nombre, email, telefono, departamento, salario) #El constructor del profesor no incluia el salario
        else:
            return None
    except ValueError:
        pass
    except IndexError:
        pass

def cargar_desde_csv(ruta, separador=",", encoding="utf-8"):
    try:
        if not os.path.exists(ruta):
            raise ArchivoNoEncontradoError('No se encuentra el archivo.')
        with open(ruta, "r", encoding=encoding) as f:
            personas = []
            lineas = f.readlines()
            for linea in lineas: #Y otros dos puntos
                if linea.strip() == "":
                    continue
                campos = linea.strip().split(separador)
                p = crear_persona_desde_campos(campos)
                if p != None:
                    personas.append(p)
    except ArchivoNoEncontradoError as e:
        print(e)
    else:
        return personas


def buscar_por_nombre(personas, texto, modo="exacto", ignore_case=True):
    for p in personas:
        nombre = p.nombre
        if ignore_case:
            nombre = nombre.lower()
            texto = texto.lower()

        if modo == "exacto":
            if nombre == texto:
                return p
        elif modo == "parcial":
            if texto in nombre:
                return p
    return None


def resumen_general(personas):
    total = len(personas)
    alumnos = [p for p in personas if isinstance(p, Alumno)]
    profesores = [p for p in personas if isinstance(p, Profesor)]
    medias = []
    for a in alumnos:
        if a.notas != []:
            medias.append(a.media(a.notas))
        else:
            medias.append(0)

    media_global = sum(medias) / len(medias)
    return total, len(alumnos), len(profesores), media_global


def exportar_resumen(personas, ruta_salida):
    salida = "tipo;nombre;email;curso;media\n"
    for p in personas:
        if isinstance(p, Alumno):
            if p.notas != []: #Manejar errores en caso de que no tenga notas
                salida += f"A;{p.nombre};{p.email};{p.grupo};{p.media(p.notas):.2}\n"
            else:
                salida += f"A;{p.nombre};{p.email};{p.grupo};media= 0,00\n"
        elif isinstance(p, Profesor):
            salida += f"P;{p.nombre};{p.email};{p.departamento};{p.salario}\n"
        else:
            salida += f"?;{p.nombre};{p.email};-\n"

    open(ruta_salida, "w").write(salida)


def validar_email(email):
    try:
        if not re.search(r"[^\s][A-Za-z\d\W]{7,16}@[a-z]{4,10}\.[a-z]{2,4}$", email):
            raise EmailError('Email incorrecto')
    except EmailError as e:
        print(e)
    else:
       return True


def main():
    ruta = input("Ruta CSV: ")
    personas = cargar_desde_csv(ruta) #Implemento Control de Errores en el propio metodo, evitando tener que hacerlo cada vez que se llame a la funcion
    texto = input("Buscar nombre: ")
    try:
        encontrado = buscar_por_nombre(personas, texto, modo="parcial", ignore_case=True)
        if encontrado:
            """if encontrado:
                    if validar_email(encontrado.email):
                        print("Email valido")
                    else:
                        print("Email invalido")
                    
                    No borro pero desactivo este bloque, ya compruebo el mail"""

            print("Resumen:", encontrado.resumen())
        else:
            print("No encontrado")
        total, nalum, nprof, media_global = resumen_general(personas)
        print(f'Total: {total} | Alumnos: {nalum} | Profesores: {nprof} | Media global: {media_global:.2}')
    except ValueError:
        pass

    exportar_resumen(personas, "salida.csv")
    print("Exportado a salida.csv")

main()
