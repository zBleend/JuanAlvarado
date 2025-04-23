Algoritmo livieno_pesado_citycar
	Escribir "Ingrese un numero de vehiculos"
	Leer num
	Para i<-1 Hasta num Con Paso 1 Hacer
		Escribir "Auto Liviano (1) , pesado(2), citycar (3)"
		Leer auto
		Si auto==2 Entonces
			Escribir "Vehiculo pesado, costo $5000"
			total=total+5000
		SiNo
			Si auto==1 Entonces
				Escribir "Vehiculo liviano, costo $3500"
				total=total+3500
			SiNo
				Si  auto==3 Entonces
					Escribir "Vehiculo citycar, costo $2000"
					total=total+2000
				SiNo
					Escribir "Error, elija una opcion valida"
				Fin Si
			Fin Si
		Fin Si
	Fin Para
	Escribir "Las ganancias diarias son $", total
	Escribir "Las ganancias diarias con IVA son $", total*1.19
FinAlgoritmo
