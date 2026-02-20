#Aquí declaramos la clase "coche"
class coche:
    #En el constructor, queremos que se introduzcan la marca, el modelo y el año, como argumentos.
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    #Con este metodo decimos la descripción del coche
    def descripcion(self):
        print(f"La marca del coche es {self.marca}, el modelo {self.modelo} y es del año {self.año} y hago SUTUTUTUTUTUTU")

def main():
    cochaso = coche("Toyota", "Supra", "1998")
    cochaso.descripcion() #Que guapo, un Toyota Supra

main()