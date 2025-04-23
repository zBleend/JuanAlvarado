Proceso Cual_es_el_numero_mayor
	Escribir "Vamos a ver cual es tu numero mayor";
	Definir n1, n2, n3 Como Entero;
	Escribir "Escribe tu primer numero (NO INGRESAR LETRAS)";
	leer n1;
	Escribir "Escribe tu segundo numero (NO INGRESAR LETRAS)";
	leer n2;
	Escribir "Escribe tu tercer numero (NO INGRESAR LETRAS)";
	leer n3;
	SI n1 = n2 y n1 = n3 Entonces
		Escribir "Todos los numero son iguales";
	SiNo
		si n1>n2 y n1>n3 Entonces
			Escribir "Tu numero mayor es: ", n1;
		SiNo
			si n2>n3 Entonces
				Escribir "Tu numero mayor es: ", n2;
			SiNo
				Escribir "Tu numero mayor es; ", n3;
			FinSi
		FinSi
	FinSi
FinProceso
