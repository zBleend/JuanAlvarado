Algoritmo prom_notas_multi_alumno
	Definir  cant,cNotas Como Entero
	Definir n1,prom, suma Como Real
	Escribir "numero de alumnos?"
	Leer cant
	
	Para i<-1 Hasta cant Con Paso 1 Hacer
		Escribir "Cuantas notas son para el alumno ",i,"?"
		Leer cNotas
		suma=0
		Para j<-1 Hasta cNotas Con Paso 1 Hacer
			
			Escribir "Ingrese una nota"
			Leer n1
			suma=suma+n1
		Fin Para
		
		prom=suma/cNotas
		Escribir "Su promedio es ", prom
		Si prom>=4 Entonces
			Escribir "Usted Aprobo"
		SiNo
			Escribir "USted se quedó pegado"
		Fin Si
	Fin Para
	
FinAlgoritmo
