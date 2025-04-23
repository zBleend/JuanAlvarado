Algoritmo Consurso
	Definir j2, j1, meta, turno Como Entero
	Definir resp, jug1, jug2 Como Caracter
	j2=0
	j1=0
	meta =3
	turno=0
	Escribir "Ingrese jugador 1"
	Leer jug1
	Escribir "Ingrese jugador 2"
	Leer jug2
	Escribir "Bienvenido al concurso!"
	
	Mientras j2<meta o j1<meta Hacer
		Si turno MOD 2==0 Entonces
			Escribir "Turno de ",jug1
			Escribir "Contestó correctamente?"
			Leer resp
			Si resp=="si" Entonces
				j2=j2+1
			Fin Si
		SiNo
			Escribir "Turno de ", jug2
			Escribir "Contestó correctamente?"
			Leer resp
			Si resp=="si" Entonces
				j1=j1+1
			Fin Si
		Fin Si
		turno=turno+1
	Fin Mientras
	
	Si j2>j1 Entonces
		Escribir "Ganó ", jug2
	SiNo
		Escribir "Ganó ", jug1
	Fin Si
	
FinAlgoritmo
