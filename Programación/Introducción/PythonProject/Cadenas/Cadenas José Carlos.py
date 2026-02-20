#Vamos a ver los distintos métodos de usar las cadenas.


print("Usamos count para contar la cantidad de veces que se repite un valor")
cadena = "12312ABC"
cadena1 = "12345"
cadena2 = "123.12"
cadena3 = "ABC"
cadena4 = "abc"
cadena5 = "hola tronco esto es una movida"
cadena6 = "             hola tio       "
h = cadena.count("1")

print("La cantidad de 1 que hay en cadena es:",h)

print("----------------------------------------------")
print("Usamos find e index para saber dónde se encuentra un valor de la cadena, pudiendo introducir el rango de valores a analizar")

h1 = cadena.find("1", 0,7)

print(f"El número 1 se encuentra en la posición {h1}")

h2 = cadena.index("A")
print(f"La letra A se encuentra en la posición: {h2}")

print("----------------------------------------------")
print("startswith se utiliza para verificar que una cadena comienza con el valor indicado")
h3 = cadena.startswith("1")

print("Si la cadena comienza con 1 escribe true", h3)
print("Por el contrario, endswith te indica si la cadena termina con ese valor")
h4 = cadena.endswith("C")
print(h4)

print("----------------------------------------------")
print("isdigit se utiliza para saber si los valores de una cadena son dígitos")
h5 = cadena.isdigit()
print(h5)

print("Aun así, isnumeric se usa para saber si los valores de una cadena son números enteros positivos.")
h6 = cadena1.isnumeric()
print("¿Cadena1 tiene solo números enteros positivos?",h6)

print("----------------------------------------------")
print("La utilidad de isdecimal es saber si la cadena es un número entre 0 y 9.")

h7 = cadena1.isdecimal()
print(h7)

print("----------------------------------------------")
print("Se usa isalpha para saber si los valores de la cadena están dentro del alfabeto")
h8 = cadena3.isalpha()
print(f"La cadena {cadena3} está compuesta por letras del alfabeto?", h8)

print("----------------------------------------------")

print("Capitalize se usa para convertir el primer valor de una cadena en mayuscula")
h9 = cadena4.capitalize()
print(f"la cadena4 es {cadena4}, pero si uso capitalize se convierte en:", h9)

print("----------------------------------------------")
print("convierte la primera letra de cada palabra de la cadena en mayuscula")
ha = cadena5.title()
print(ha)

print("----------------------------------------------")
print("upper convierte toda la cadena en mayusculas")
hb = cadena5.upper()
print(hb)

print("----------------------------------------------")
print("Te dice si todos los caracteres de una cadena son mayusculas")
hc = cadena5.isupper()
hd = cadena3.isupper()
print(f"¿la cadena {cadena5} es toda mayuscula?", hc, f"\n¿y la cadena {cadena3}?", hd)

print("----------------------------------------------")
print("Convierte una cadena en minúscula")
he = cadena3.lower()
print(f"La cadena {cadena3} es todo minuscula pero si hacemos.... OJO: {he}")

print("----------------------------------------------")
print("islower te dice si todos los caracteres de la cadena son minúsculas")
hf = cadena3.islower()
print(hf)

print("----------------------------------------------")
print("Encode sirve para transformar una cadena a bytes usando la codificación que elijas, sino, se usará UTF-8 ")
hg = cadena.encode()
print(hg)

print("----------------------------------------------")
print("center, ljust y rjust se utilizan para alinear en un texto la cadena.")
hh = cadena5.center(200)
print("Con center pasa esto:\n",hh)

hi = cadena5.ljust(200)
print("Con ljust pasa esto:\n",hi,"\n")
hj = cadena5.rjust(200)
print("Con rjust pasa esto:\n",hj)

print("----------------------------------------------")
print("strip se utiliza para eliminar todos los espacios en blanco innecesarios de los lados de una cadena, con lstrip los de la izquierda y rstrip los de la derecha ")
hk = cadena6.strip()
print("Esto",hk,"es para probar")
hl = cadena6.lstrip()
print("Esto", hl, "es lstrip")
hm = cadena6.rstrip()
print("Esto", hm, "es rstrip")

print("----------------------------------------------")
print("Se utiliza para cambiar una parte de la cadena por otra")
hn = cadena5.replace("tronco","colega")
print(f"Antes era {cadena5} y ahora es {hn}.")

print("----------------------------------------------")
print("Este comando se usa para convertir una cadena en un elemento de una lista lista")
hñ = cadena1.split()
print(hñ)

print("----------------------------------------------")
print("Divide una cadena en partes y las convierte en partes de una lista")
ho = cadena.splitlines()
print(ho)

print("----------------------------------------------")
print("Coje distintos objetos iterables y los une en una cadena, separandolos por el elemento que elijas")
hner = ("Loco","Verde","Roto")
hp = ",".join(hner)
print(hp)

print("----------------------------------------------")
print("Se usa format para poder definir el formato o introducir distintas variables de una cadena")
decimal = float(1.215465321654)
print(f"La cadena {decimal} es así de larga pero si hacemos esto: decimal:.2f.... {decimal:.2f}.")

print("----------------------------------------------")
print("Se usa para reemplazar o eliminar caracteres de una cadena según un diccionario de traducción creado por str.maketrans().")

data = str.maketrans("aeiou","12345")
hq = cadena5.translate(data)
print(hq)