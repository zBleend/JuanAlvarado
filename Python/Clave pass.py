import os
import time
user=None
clave=None
while True:
    print("Bienvenido al sistema")
    resp=input("1.- Iniciar sesion\n2.- Registrarse\n3.- Salir\n")
    while resp not in ["1", "2", "3"]:
        resp=input("Ingrese una opcion valida\n")
    if resp=="2":
        os.system('cls')
        user=input(f"Ingrese un nombre para registrarse: \n")
        clave=input(f"Ingrese una clave para registrarse: \n")
        print("Listo, ya se encuentra en el sistema")
    elif resp=="1":
        if user is None or clave is None:
            print("No hay nadie registrado, ¡Se el primero!")
            time.sleep(1)
            os.system('cls')
        else:
            os.system('cls')
            user1=input("Ingrese su nombre: \n")
            clave1=input("Ingrese su clave: \n")
            while True:
                if user1==user and clave1==clave:
                    print(f"Bienvenido {user} al sistema")
                    salir=True
                    break
                else:
                    print("Error, nombre o clave erroneo\n")
        if salir:
            break
    elif resp=="3":
        print("Adios...")
        break
        