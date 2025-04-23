Algoritmo carrito_para
	Definir cant, prod Como Entero
	Definir total como Real
	
	//Escribir "Cuantos productos comprará?"
	//Leer cant
	
	Mientras total<10000 Hacer
	
			Escribir "Selecciones un producto"
			Escribir "1.- Vaselina $ 2000"
			Escribir "2.- Rimel $ 3000"
			Escribir "3.- Algodon $4000"
			Leer prod
			Si prod==1 Entonces
				total=total+2000
				Si total>10000 Entonces
					total=total-2000
				Fin Si
			SiNo
				Si prod==2 Entonces
					total=total+3000
				SiNo
					Si prod==3 Entonces
						total=total+4000
					SiNo
						Escribir "Error, seleccione una opcion valida"
					Fin Si
				Fin Si
			Fin Si

			Escribir "El total actual es $", total
	
	Fin Mientras
	
	
	Escribir "El total mas IVA es $", total*1.19
FinAlgoritmo
