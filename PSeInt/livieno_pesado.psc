Algoritmo livieno_pesado
	Escribir "Ingrese un numero de vehiculos"
	Leer num
	//pedir un numero a un usuario 
	//de cuantos vehiculos entran al ´parking
	//Si el vehiculo es pesado cobrar 5000
	// si el vehiculo es liviano cobrar 3000
	//mostrar ganncias al final
	Para i<-1 Hasta num Con Paso 1 Hacer
		Escribir "Auto Liviano (1) o pesado(2)"
		Leer auto
		Si auto==1 Entonces
			Escribir "Vehiculo pesado, costo $5000"
			total=total+5000
		SiNo
			Escribir "Vehiculo liviano, costo $3000"
			total=total+3000
		Fin Si
	Fin Para
	
	Escribir "Las ganancias diarias son $", total
FinAlgoritmo
