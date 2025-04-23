Proceso El_mayor_de_tres
	Definir n1, n2, n3 Como Entero;
	Escribir 'Introduce tus numeros';
	Escribir 'introduce tu primer numero: ';
	Leer n1;
	Escribir 'introduce tu segundo numero: ';
	Leer n2;
	Escribir 'introduce tu ultimo numero: ';
	Leer n3;
	Si n1>n2 Y n1>n3 Entonces
		Escribir 'tu numero mayor es: ', n1;
	SiNo
		Si n2>n3 Entonces
			Escribir 'tu numero mayor es: ', n2;
		SiNo
			Escribir 'Tu numero mayor es: ', n3;
		FinSi
	FinSi
FinProceso
