Algoritmo sin_titulo
	Limpiar Pantalla
	Escribir "ingrese la cantidad de vehiculos que ingresan"
	leer num
	
	para i<-1 Hasta num Con Paso 1 Hacer
		Escribir "¿cual es el peso?"
		Escribir "Pesado"
		Escribir "Liviano"
		leer peso
		si peso == "pesado" Entonces
			total=total+5000
		finsi
		si peso=="liviano" Entonces
			total=total+3000
		FinSi
	FinPara
	Escribir "La cantidad de vehiculos es: ",num " y el total a pagar es: $",total
FinAlgoritmo
