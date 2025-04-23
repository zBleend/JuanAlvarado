Algoritmo cuenta_impar
	Escribir "Ingrese un numero"
	Leer num
	Para i<-1 Hasta num Con Paso 1 Hacer
		Si i MOD 2<>0 Entonces
			//Escribir "El numero ", i , " es par"
			Escribir i
			contador=contador+1
		SiNo
			//Escribir "El numero ", i , " es impar"
		Fin Si
	Fin Para
	Escribir "La cantidad de numeros impares es ", i
	
FinAlgoritmo
