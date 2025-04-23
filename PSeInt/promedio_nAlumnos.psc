Algoritmo promedio_nAlumnos
	Definir cant , cNotas Como Entero
	Definir n1, n2, n3, suma, prom Como Real
	Escribir "Cuantos alumnos son?"
	Leer cant
	
	Para i<-1 Hasta cant Con Paso 1 Hacer
		Escribir "Notas del alumno ", i
		Escribir "Cuantas notas son?"
		Leer cNotas
		suma=0
		Para j<-1 Hasta cNotas Con Paso 1 Hacer
			Escribir "Ingrese la nota numero ",j
			Leer n1
			suma=suma+n1
		Fin Para
		prom=suma/cNotas
		Escribir "El promedio del alumno ", i, " es ", prom
		Si prom<4 Entonces
			Escribir "Reprobó"
		SiNo
			Escribir	"Felicidades, aprobó"
		Fin Si
	Fin Para
	
FinAlgoritmo
