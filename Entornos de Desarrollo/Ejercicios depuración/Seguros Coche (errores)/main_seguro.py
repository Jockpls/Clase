from coche_seguro import CocheSeguro
from seguro import Seguro

def main():
    tipo = input("Tipo de coche (Turismo/Deportivo/Furgoneta): ").strip()
    antig = int(input("Años de antigüedad: "))
    cobertura = input("Cobertura (Básica/Completa): ").strip()
    multas = int(input("Número de multas del conductor: "))

    coche = CocheSeguro(tipo, antig)
    seguro = Seguro(coche, cobertura, multas)

    print(f"Precio final del seguro: {seguro.precio_total()}€")

if __name__ == "__main__":
    main() 
