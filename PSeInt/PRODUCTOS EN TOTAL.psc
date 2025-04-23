Algoritmo sin_titulo
	Limpiar Pantalla
	Escribir "*******************************"
	Escribir "          Bienvenido		  "
	Escribir "*******************************"
	Escribir " "
	Esperar 1 segundos
	Escribir "*******************************"
	Escribir "¿Cuantos productos va a llevar?"
	Escribir "*******************************"
	Leer num
	prodtotal<-num
	Esperar 1 Segundos
	Limpiar Pantalla
	Escribir "*******************************"
	Escribir "    Usted lleva ", num, " Productos"
	Escribir "*******************************"
	Escribir " "
	Esperar 1 Segundos
	Limpiar Pantalla
	Escribir "*******************************"
	Escribir "      Elija sus productos (",num ")"
	Escribir "*******************************"
	Escribir "1.- Pan $500"
	Escribir "2.- Leche $1500"
	Escribir "3.- Carne $4000"

	para i<-1 Hasta num Con Paso 1 Hacer
		leer prod
			prod= Minusculas(prod)
			si prod == "carne" Entonces
				total=total+4000
				Escribir "Usted lleva carne (Restantes: ", num-1 ")"
			FinSi
			si prod=="leche" Entonces
				total=total+1500
				Escribir "Usted lleva leche (Restantes: ", num-1 ")"
			FinSi
			si prod=="pan" Entonces
				total=total+500
				Escribir "Usted lleva pan (Restantes: ", num-1 ")"
			FinSi
			num=num-1
	FinPara
	Esperar 1 Segundos
	Limpiar Pantalla
	Escribir "*******************************"
	Escribir "Resumen de compra:"
	Escribir "Cantidad de productos: ", prodtotal
	Escribir "Total a pagar: $", total
	Escribir "Gracias por su compra."
	Escribir "*******************************"
FinAlgoritmo