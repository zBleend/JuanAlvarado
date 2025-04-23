Algoritmo votos
	Escribir "ingrese un numero de votantes"
	Leer num
	
	kaiser=0
	nose=0
	
	Para i<-1 Hasta num Con Paso 1 Hacer
		Escribir "ingrese su voto: Kaiser 1, Nose 2"
		Leer voto
		Si voto==1 Entonces
			kaiser=kaiser+1
		SiNo
			Si voto==2 Entonces
				nose=nose+1
			SiNo
				Escribir "Error, selecione un voto válido"
			Fin Si
		Fin Si
	Fin Para
	Escribir "los votos de Kaiser son ",kaiser
	Escribir "los votos de Nose son ",nose
	Si kaiser>nose Entonces
		Escribir "Gano Kaiser"
	SiNo
		Escribir "Gano Nose"
	Fin Si
FinAlgoritmo
