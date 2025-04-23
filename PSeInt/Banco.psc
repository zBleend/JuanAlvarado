Proceso Banco
	
	Definir Saldo, Menu, Transferencia, Final, Seguridad, Monto, Intentos Como Entero;
	Definir Usuario, Usuario_DATA, Contrasena, Contrasena_DATA, SN, Usuario_transferencia Como Caracter;
	
	Saldo = 10000;
	Final = 0;
	Usuario_DATA = "";
	Contrasena_DATA = "";
	Intentos = 3;
	Menu = 0;
	Monto = 0;
	
	Repetir
		Limpiar Pantalla;
		Escribir "***********************************                               ",HoraActual();
		Escribir "Bienvenido al banco (Let me cook)";
		Escribir "***********************************";
		Escribir "1. Iniciar sesion";
		Escribir "2. Registrarse";
		Escribir "3. Salir";
		leer Final;
		
		Esperar 2 segundos;
		Limpiar Pantalla;
		
		Mientras Final == 1 Hacer
			
			Escribir "Digite su nombre de usuario";
			Leer Usuario;
			Escribir "Digite su contraseña";
			leer Contrasena;
			
			Repetir
				si Usuario == Usuario_DATA y Contrasena == Contrasena_DATA Entonces
					
					Limpiar Pantalla;
					Esperar 0.5 segundos;
					
					Escribir "Has iniciado sesion correctamente";
					Limpiar Pantalla;
					Esperar 0.5 segundos;
					
					Escribir "Cargando.";
					Esperar 0.5 segundo;
					Limpiar Pantalla;
					Escribir "Cargando..";
					Esperar 0.5 segundo;
					Limpiar Pantalla;
					Escribir "Cargando...";
					Esperar 1 segundo;
					Limpiar Pantalla;
					
					Mientras Menu == 0 Hacer
						
						Escribir "***********************************";
						Escribir "      Banco (Let me cook)";
						Escribir "***********************************";
						Escribir "1. Ver saldo";
						Escribir "2. Transferir";
						Escribir "3. volver atras";
						leer Menu;
						
						Mientras Menu == 1 Hacer
							
							Limpiar Pantalla;
							Escribir "Su saldo es: ",saldo;
							Esperar 2 segundos;
							Limpiar Pantalla;
							
							Menu = 0;
							
						FinMientras
						
						Mientras Menu == 2 Hacer
								
							Limpiar Pantalla;
							Escribir "Digite el nombre del usuario al que desea transferir";
							leer Usuario_transferencia;
							Escribir "Digite la cantidad que desea transferir";
							Escribir "(Monto actual: ",Saldo,")";
							leer Monto;
								
							Limpiar Pantalla;
							Esperar 0.5 segundos;
								
							Escribir "Para confirmar la transferencia digite su contraseña";
							leer Contrasena;
								
							si Contrasena <> Contrasena_DATA y Intentos > 0 Entonces
								
								Escribir "Contraseña incorrecta";
								Escribir "Vuelva a intentarlo";
								Escribir "Intentos restantes: ",Intentos;
								Intentos = Intentos - 1;
								Esperar 2 segundos;
							SiNo
								si Intentos == 0 Entonces
									
									Limpiar Pantalla;
									Escribir "Numero de intentos sobrepasado";
									Escribir "Bloqueando cuenta....";
									Menu = 3;
									Final = 0;
									
								FinSi
								
							FinSi
								
							si  Contrasena == Contrasena_DATA Entonces
								
								Limpiar Pantalla;
								saldo = saldo - Monto;
								Escribir "Transferencia realizada con exito";
								Escribir "Saldo restante: ",saldo;
								Esperar 2 segundos;
								Menu = 0;
								Limpiar Pantalla;
								
							FinSi
							
						FinMientras
							
						si Menu == 3 Entonces
							
							Final = 0;
							
						FinSi
						
					FinMientras
				FinSi
				
				si Usuario <> Usuario_DATA o Contrasena <> Contrasena_DATA Entonces
					
					Escribir "Hubo un erro al iniciar sesion";
					Escribir "El usuario o la contraseña ingresados son incorrectos";
					Esperar 2 segundos;
					Menu = 3;
					Final = 0;
					
					
				FinSi
			Hasta Que Menu == 3
			
		FinMientras
		
		Mientras Final == 2 Hacer
			
			Escribir "Digite el nombre de usuario que desea registrar";
			leer Usuario_DATA;
			Escribir "Digite su contraseña";
			Leer Contrasena_DATA;
			
			Limpiar Pantalla;
			Seguridad = Longitud(Contrasena_DATA);
			
			Mientras Seguridad <10 Hacer
				
				Limpiar Pantalla;
				Escribir "Su contraseña es muy corta";
				Escribir "Por temas de seguridad su contraseña";
				Escribir "debe contar como minimo con 10 caracteres";
				
				Esperar 0.5 segundo;
				
				Escribir "Digite su contraseña";
				Leer Contrasena_DATA;
				Seguridad = Longitud(Contrasena_DATA);
				
			FinMientras
			
			Limpiar Pantalla;
			Escribir "Su Usuario es: ",Usuario_DATA;
			Escribir "Su contraseña es: ",Contrasena_DATA;
			Escribir "Estos datos son correctos?";
			Escribir "[Si/No]";
			Leer SN;
			
			si SN == Minusculas("no") Entonces
				
				Escribir "Digite el nombre de usuario que desea registrar";
				leer Usuario_DATA;
				Escribir "Digite su contraseña";
				Leer Contrasena_DATA;
				
				Limpiar Pantalla;
				Escribir "Su Usuario es: ",Usuario_DATA;
				Escribir "Su contraseña es: ",Contrasena_DATA;
				Escribir "Estos datos son correctos?";
				Escribir "[Si/No]";
				Leer SN;
				
			FinSi
			
			Limpiar Pantalla;
			Escribir "Usuario y contraseña registrados con exito";
			Esperar 1 segundo;
			Final = 0;
			
		FinMientras
		
		
		Limpiar Pantalla;
	Hasta Que Final = 3
FinProceso
