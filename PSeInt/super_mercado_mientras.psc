Algoritmo super_mercado_mientras

	//Preguntar al usuario cuantos productos llevar�
	// escribir listado de 3 productos y sus precios
	//mostrar el total neto de la compra
	// y mostrar el total mas IVA (19%)
	
	Definir cant, total, op Como Entero
	//Escribir "Cuantos productos llevar�?"
	//Leer cant
	
	Mientras total<=10000 Hacer
		Escribir "El total actual es ", total
		Escribir "Que producto llevar�?"
		Escribir "1.- Diazepam $9000"
		Escribir "2.- Metametozona $18500"
		Escribir "3.- Oblea China $1000"
		Leer op
		
		Si op==1 Entonces
			Escribir "Usted lleva dIAZEPAM"
			total=total+9000
			
		SiNo
			Si op==2 Entonces
				Escribir "Usted lleva Metametozona"
				total=total+18500
			SiNo
				Si op==3 Entonces
					Escribir "Usted lleva Oblea China"
					total=total+1000
				SiNo
					Escribir "Error, selecione una opcion valida (1,2,3)"
				Fin Si
			Fin Si
		Fin Si
	Fin Mientras
		
		

	
	Escribir "EL total neto es ", total
	Escribir "EL total mas IVA es ", total*1.19
FinAlgoritmo
