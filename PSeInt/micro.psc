Algoritmo micro
	Definir distancia, distancia_recorrida, Pmicro, gente Como Entero
	
	Escribir "Cuanta distancia recorrera?"
	Leer distancia
	
	Mientras distancia>distancia_recorrida Hacer
		Escribir "Llegó al paradero"
		Escribir "Cuanta gente sube?"
		Leer gente
		Pmicro=Pmicro+gente
		Mientras Pmicro>80 Hacer
			Pmicro=Pmicro-gente
			Escribir "Estamos llenos, suba menos gente"
			Escribir "Cuanta gente sube?"
			Leer gente
			Pmicro=Pmicro+gente
		Fin Mientras
		Escribir "Los pasajeros actuales son ", Pmicro
		Escribir "Cuanta gente baja?"
		Leer gente
		Pmicro=Pmicro-gente
		Escribir "Los pasajeros actuales son ", Pmicro
		distancia_recorrida=distancia_recorrida+5
	Fin Mientras
	
	Escribir "Ha llegado al destino"
FinAlgoritmo
