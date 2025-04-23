Algoritmo concurso
	j1=0
	j2=0
	score=3
	cont=1
	
	Mientras j1<score o j2<score Hacer
		Si cont MOD 2==0 Entonces
			Escribir "Turno de Jugador 1"
			Escribir "es correcto?"
			Leer resp
			Si resp=="si" Entonces
				j1=j1+1
			Fin Si
		SiNo
			Escribir "turno de Jugador 2"
			Escribir "es correcto?"
			Leer resp
			Si resp=="si" Entonces
				j2=j2+1
			Fin Si
		Fin Si
		cont=cont+1
	
	Fin Mientras
	Si j1<j2 Entonces
		Escribir "Jugador 2 Gana!"
	SiNo
		Escribir "Jugador 1 gana!"
	Fin Si
	
	
FinAlgoritmo
