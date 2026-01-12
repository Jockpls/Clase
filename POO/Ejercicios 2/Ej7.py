from abc import ABC, abstractmethod
from beartype import beartype

@beartype
class Pipeline(ABC):        #Clase abstracta padre
    @abstractmethod         #Metodo abstracto
    def ejecutar(self):
        pass


class PipelineCSV(Pipeline):         #Hija
    def __init__(self, archivo):
        self.archivo = archivo

    def ejecutar(self):              #Implementamos metodo abstracto
        if self.archivo[-4:] == ".csv" :    #Mediante slicing, comprobamos la extensión del archivo
            return f"Correcto miarma, ejecutando"
        else:
            return f"Esto que eeeeeeeeee"


class PipelineJSON(Pipeline):  # Hija
    def __init__(self, archivo):
        self.archivo = archivo

    def ejecutar(self):  # Implementamos metodo abstracto
        if self.archivo[-5:] == ".JSON":  # Mediante slicing, comprobamos la extensión del archivo
            return f"Correcto miarma, ejecutando"
        else:
            return f"Esto que eeeeeeeeee"


class PipelineAPI(Pipeline):  # Hija
    def __init__(self, archivo):
        self.archivo = archivo

    def ejecutar(self):  # Implementamos metodo abstracto
        if self.archivo[-4:] == ".api":  # Mediante slicing, comprobamos la extensión del archivo
            return f"Correcto miarma, ejecutando"
        else:
            return f"Esto que eeeeeeeeee"

def main():
    csv = PipelineCSV("prueba.csv")
    print(csv.ejecutar())
    JSON = PipelineJSON(".JSONN")
    print(JSON.ejecutar())
    API = PipelineAPI(".api")
    print(API.ejecutar())

main()