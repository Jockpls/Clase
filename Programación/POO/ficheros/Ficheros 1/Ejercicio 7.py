with open('lenguajes.txt','rt') as f: #En una linea designamos a f como objeto y con with evitamos tener que cerrarlo.
    lines = f.readlines()   #Leemos todas las lineas del fichero y las introducimos en la variable lines
    for n, line in enumerate(lines):    #n para ver cuántos tenemos y mediante line vamos recorriendo el documento en lines
        print(n+1, line.rstrip())   #Mostramos por pantalla sin saltos de linea excesivos
'''El uso de with permite simplificar y ahorrar tiempo de programación, evitando posibles errores cómo que se olvide cerrar el fichero'''