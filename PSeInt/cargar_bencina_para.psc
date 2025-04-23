Algoritmo cargar_bencina_para
	Escribir "Ingrese la cantidad de autos"
	Leer num
	total=0
	Para i<-1 Hasta num Con Paso 1 Hacer
		Escribir "Cual bencina cargará?"
		Escribir "93 - Normal $800"
		Escribir "95 - Normal $1000"
		Escribir "97 - Normal $1500"
		Leer b
		Si b==93 Entonces
			Escribir "Usted carga bencina normal"
			Escribir "Cuantos litros va a cargar?"
			Leer lt
			costo=800*lt
			total=total+costo
			Escribir "Usted cargó ", lt, " litros de combustible normal y el total es ", costo
		SiNo
			Si b==95 Entonces
				Escribir "Usted carga bencina plus"
				Escribir "Cuantos litros va a cargar?"
				Leer lt
				costo=1000*lt
				total=total+costo
				Escribir "Usted cargó ", lt, " litros de combustible plus y el total es ", costo
				
			SiNo
				Si b==97 Entonces
					Escribir "Usted carga bencina premium"
					Escribir "Cuantos litros va a cargar?"
					Leer lt
					costo=1500*lt
					total=total+costo
					Escribir "Usted cargó ", lt, " litros de combustible premium y el total es ", costo
					
				SiNo
					Escribir "Error, seleccione un octanaje válido."
				Fin Si
			Fin Si
			
		Fin Si
	Fin Para
	Escribir "El total de ventas es ", total
FinAlgoritmo
