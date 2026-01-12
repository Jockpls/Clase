def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        return [f"Mover disco 1 desde {origen} hasta {destino}"]
    return (
            hanoi(n - 1, origen, destino, auxiliar)
            + [f"Mover disco {n} desde {origen} hasta {destino}"]
            + hanoi(n - 1, auxiliar, origen, destino)
    )
def main():
    n = int(input("Introduce el número de discos: "))
    pasos = hanoi(n, "A", "B", "C")
    for paso in pasos:
        print(paso)

main()