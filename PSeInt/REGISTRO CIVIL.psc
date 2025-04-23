Algoritmo sin_titulo
	//la capacidad maxima del registro civil es de 500 personas x dia, en el lobby caben solo 100, ordenar para que pasen en grupos pequeños y descontar cuando hagan su tramite,
	//crear programa para meter gente a hacer tramietes y cada tramite cuesta un valor aleatorio entre 4000 y 30000 pesos, mostrar ganancias
	Definir costo Como Entero
	Repetir
		Repetir
			Escribir "Bienvenido al registro civil"
			Esperar 1 Segundos
			Escribir "Ingrese su nombre"
			leer nom
			Escribir "Ingrese su rut"
			Escribir "Si no tiene ponga 0"
			leer rut
			Escribir "Ingrese su correo"
			leer correo
			Limpiar Pantalla
			Escribir "Cargando..."
			Esperar 2 Segundos
			Limpiar Pantalla
			Escribir "Hola ", nom, " Bienvenido"
			Escribir "¿Que tramite viene a hacer?"
			Escribir " "
			Escribir "1.- Inscripción de nacimientos"
			Escribir "2.- Inscripción de matrimonios"
			Escribir "3.- Inscripción de profesionales"
			Escribir "4.- Inscripción de cambios de nombre y apellidos"
			Escribir "5.- Inscripción de cédulas de identidad para extranjeros"
			Escribir "6.- Salir"
			leer op
			costo=Aleatorio(4000,30000)
			segun op Hacer
				1:
					Esperar 1 Segundos
					Limpiar Pantalla
					Escribir "Inscripcion de nacimiento"
					Escribir "Ingrese el nombre del recien nacido"
					leer nom2
					Escribir "Ingrese numero de documento"
					leer doc1
					Escribir "Listo, su inscripcion está lista"
					Esperar 1 Segundos
					Escribir "Sus resultados serán enviados por correo (", correo, ")"
					Escribir "Pase a caja para pagar: ", costo, "(incluye IVA)"
					costototal=0+costo
					Esperar 5 Segundos
					op=6
					gente=gente+1
				2:
					Esperar 1 Segundos
					Limpiar Pantalla
					Escribir "Inscripcion de matrimonio"
					Escribir "Ingrese el primer nombre"
					leer nom3
					Escribir "Ingrese rut"
					leer doc2
					Escribir "Ingrese el segundo nombre"
					leer nom4
					Escribir "Ingrese rut"
					leer doc3
					Escribir "Listo, su inscripcion de matrimonio está lista"
					Esperar 1 Segundos
					Escribir "Sus resultados serán enviados por correo (", correo, ")"
					Escribir "Pase a caja para pagar: ", costo, "(incluye IVA)"
					costototal=0+costo
					Esperar 5 Segundos
					op=6
					gente=gente+1
				3: 
					Esperar 1 Segundos
					Limpiar Pantalla
					Escribir "Inscripcion de profesion"
					Escribir "Ingrese su profesion"
					leer prof
					Escribir "Su profesion está a nombre de: ", nom
					Escribir "Listo, su inscripcion de matrimonio está lista"
					Esperar 1 Segundos
					Escribir "Sus resultados serán enviados por correo (", correo, ")"
					Escribir "Pase a caja para pagar: ", costo, "(incluye IVA)"
					costototal=0+costo
					Esperar 5 Segundos
					op=6
					gente=gente+1
				4:
					Esperar 1 Segundos
					Limpiar Pantalla
					Escribir "Inscripción de cambios de nombre y apellidos"
					Escribir "Ingrese su nuevo nombre" 
					escribir "(Si quiere mantener el que tiene escriba su nombre actual)"
					leer nom5
					Escribir "Ingrese su nuevo apellido"
					escribir "(Si quiere mantener el que tiene escriba su apellido actual)"
					leer apelli
					Escribir "Su nombre es: ", nom5, " ", apelli
					Escribir "Listo, su cambio de nombre está listo"
					Esperar 1 Segundos
					Escribir "Sus resultados serán enviados por correo (", correo, ")"
					Escribir "Pase a caja para pagar: ", costo, "(incluye IVA)"
					costototal=0+costo
					Esperar 5 Segundos
					op=6
					gente=gente+1
				5:
					Esperar 1 Segundos
					Limpiar Pantalla
					Escribir "Inscripción de cédulas de identidad para extranjeros"
					Escribir "Ingrese numero de pasaporte"
					leer pasa
					Escribir "Ingrese su pais de origen"
					leer pais
					Escribir "Listo, su cambio inscripcion de cedula de identidad está lista"
					Esperar 1 Segundos
					Escribir "Sus resultados serán enviados por correo (", correo, ")"
					Escribir "Pase a caja para pagar: ", costo, "(incluye IVA)"
					costototal=0+costo
					Esperar 5 Segundos
					op=6
					gente=gente+1
				6:
					Esperar 1 Segundos
					gente=gente+1
				De Otro Modo:
					Escribir "Error seleccione una opcion valida"
					Esperar 2 Segundos
			FinSegun
			Limpiar Pantalla
		Hasta Que op=6
	Hasta Que gente=501
	Escribir "El total de ganacias de hoy es: ", costototal
FinAlgoritmo