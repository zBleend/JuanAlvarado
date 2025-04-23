Algoritmo sin_titulo
	Definir nom1, op1, op3, op6, exit Como Caracter
	Definir contador, op2, comida1, comida2, comida3, precio, precio1, precio2, precio3, preciototal, totalIva, cliente Como Entero
	Repetir
		Escribir "*****************************"
		Escribir "         BIENVENIDO"
		Escribir "*****************************"
		Esperar 1 Segundos
		Limpiar Pantalla
		Escribir "Cargando..."
		Esperar 2 Segundos
		Limpiar Pantalla
		Escribir "******************************"
		Escribir "Ingrese el nombre del cliente"
		Escribir "******************************"
		leer nom1
		cliente=cliente+1
		precio=0
		comida1=0
		comida2=0
		comida3=0
		preciototal=0
		totalIva=0
		Repetir
			Escribir "************** MENU ***************"
			Escribir "Cliente: ", nom1
			Escribir "1.- Arroz a la francesa.....$4.500"
			Escribir "2.- Arroz marinero..........$5.200"
			Escribir "3.- Sopa marinera...........$9.700"
			Escribir "4.- Finalizar menu"
			Escribir "5.- Salir del sistema"
			Escribir "***********************************"
			leer op
			Segun op Hacer
				1:
					Escribir "******************************"
					Escribir "Lleva Arroz a la francesa"
					Escribir "******************************"
					precio1=precio1+4500
					comida1=comida1+1
				2:
					Escribir "******************************"
					Escribir "Lleva Arroz marinero"
					Escribir "******************************"
					precio2=precio2+5200
					comida2=comida2+1
				3:
					Escribir "******************************"
					Escribir "Lleva Sopa marinera"
					Escribir "******************************"
					precio3=precio3+9700
					comida3=comida3+1
				4: 
					Escribir "******************************"
					Escribir "Finalizando menu..."
					Escribir "******************************"
					Esperar 2 Segundos
					Limpiar Pantalla
					Escribir "En total, el cliente lleva: "
					Escribir comida1, " de Arroz a la francesa ", precio1
					Escribir comida2, " de Arroz marinero ", precio2
					Escribir comida3, " de Sopa marinera ", precio3
					Escribir "¿Es correcto? [SI/NO]"
					leer op1
					op1= Minusculas(op1)
					Segun op1 Hacer
						"si": 
							preciototal=precio1+precio2+precio3
							Escribir "El total neto es: ", preciototal
							totalIva=((preciototal*119)/100)
							Escribir "El total a pagar (IVA) es: ", totalIva
							Esperar 1 Segundos
							Escribir "¿Quiere salir? [SI/NO]"
							Escribir "Si = salir"
							Escribir "No = Agregar algo mas"
							leer op4
							op4= Minusculas(op4)
							Segun op4 Hacer
								"si":
									op3="Cancelar"
									totalventas=totalIva+totalventas
								"no":
									op2=1
							FinSegun
						"no": 
							Escribir "¿Va a agregar algo mas o quiere cancelar?"
							Escribir "1.- Agregar"
							Escribir "2.- Cancelar"
							leer op2
							Segun op2 hacer
								1:
									Escribir "Ingrese su platillos restantes"
									Escribir " "
								2:
									Escribir "Operacion cancelada"
									op3="Cancelar"
							FinSegun
					FinSegun
				5:
					Escribir "Saliendo del sistema"
					Esperar 2 Segundos
					op3="Cancelar"
					exit="true"
			FinSegun
		Hasta Que op3="Cancelar"
	Hasta Que exit="true"
	Escribir "Total de clientes: ", cliente
	Escribir "Ventas en total: ", totalventas
FinAlgoritmo
