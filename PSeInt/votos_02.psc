Algoritmo votos
	Escribir "ingrese un numero de votantes"
	Leer num
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
		Escribir "Gano Kaiser con un ",100/num*kaiser ,"%"
	SiNo
		Si kaiser<nose Entonces
			Escribir "Gano Nose con un ",100/num*nose ,"%"
		SiNo
			Escribir "Es un empate"
		Fin Si
	Fin Si
FinAlgoritmo
