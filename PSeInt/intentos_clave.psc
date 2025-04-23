Algoritmo intentos_clave
	Definir  clave , pass, limite, intento Como Entero
	limite=3
	intento=1
	clave=7878
	Escribir "Ingrese su clave"
	Leer pass
	
	Mientras clave<>pass y intento<limite Hacer
		Escribir "Error, Ingrese su clave nuevamente, intento n°", intento
		Leer pass
		intento=intento+1
	Fin Mientras
	Si intento==limite y clave<>pass Entonces
		Escribir "Sistema bloqueado"
	SiNo
		Escribir "Bienvenido al sistema"
	Fin Si
	
FinAlgoritmo
