Algoritmo concurso_2
	Definir j1, j2, meta, turno Como Entero
	Definir resp, jugador1, jugador2 Como Caracter
	meta=3
	turno=0
	Escribir "Quienes jugaran?"
	Escribir "ingres el jugador 1"
	Leer jugador1
	Escribir "ingres el jugador 2"
	Leer jugador2
	
	Mientras j1<meta o j2<meta Hacer
		Si turno MOD  2==0 Entonces
			Escribir "Turno de ", jugador1
			Escribir "respondio bien?"
			Leer resp
			Si resp=="si" Entonces
				j1=j1+1
			Fin Si
			
		SiNo
			Escribir "Turno de ", jugador2
			Escribir "respondio bien?"
			Leer resp
			Si resp=="si" Entonces
				j2=j2+1
			Fin Si
		Fin Si
		turno=turno+1
	Fin Mientras
	Si j1>j2 Entonces
		Escribir "El ganador es ", jugador1
	SiNo
		Escribir "El ganador es ", jugador2
	Fin Si
	
FinAlgoritmo
