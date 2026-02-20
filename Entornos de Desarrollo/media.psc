Algoritmo media
	Escribir '¿De cuántos números quieres hacer la media?'
	Leer total
	x = 1
	Mientras x <= total Hacer
		Escribir "Introduce un número"
		Leer n
		suma = suma + n
		x = x + 1
	Fin Mientras
	
	aari = suma/total
	Escribir "La media es: ", aari
FinAlgoritmo
