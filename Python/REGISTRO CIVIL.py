import time
import os
import random

def total_gente():
    gente=1
    while gente<2:
        def sistema():
            print("Bienvenido al registro civil")
            time.sleep(1)
            nom=input("Ingrese su nombre:\n")
            rut=input("Ingrese su Rut:\nSi no tiene ponga 0 y enter\n")
            correo=input("Ingrese su correo:\n")
            os.system('cls')
            print("Cargando...")
            time.sleep(2)
            os.system('cls')
            print(f"Hola {nom}, Bienvenido")
            print("¿Que tramite viene a hacer?\n")
            op=int(input("1.- Inscripción de nacimientos\n2.- Inscripción de matrimonios\n3.- Inscripción de profesionales\n4.- Inscripción de cambios de nombres y/o apellidos\n5.- Inscripción de cédulas de identidad para extranjeros\n6.- Salir\n"))
            costo=random.randint(4000, 30000)
            if op==1:
                while True:
                    time.sleep(1)
                    os.system('cls')
                    print("Inscripcion de nacimiento\n------------------------------------------")
                    nacimiento=input("¿Quiere iniciar el tramite?\n[SI/NO]\n").upper()
                    while nacimiento not in ["SI", "NO"]:
                           os.system('cls')
                           print("ERROR, seleccione una opcion valida")
                           nacimiento=input("¿Quiere iniciar el tramite?\n[SI/NO]\n").upper()
                    if nacimiento=="SI":
                        bebe1=input("Ingrese el/los nombre(s) del recien nacido\n")
                        bebe2=input("Ingrese el/los apellido(s) del recien nacido\n")
                        print("Cargando...")
                        time.sleep(1)
                        resp=input(f"El nombre(s) es {bebe1} {bebe2} ¿Es correcto?[SI/NO]\n").upper()
                        while resp not in ["SI", "NO"]:
                            os.system('cls')
                            print("ERROR, seleccione una opcion valida [SI/NO]")
                            resp=input(f"El nombre(s) es {bebe1} {bebe2} ¿Es correcto?[SI/NO]\n").upper()
                        if resp=="SI":
                            nom2=input("Ingrese el nombre y apellido del padre (Si no es presente ponga NO)\n").upper()
                            if nom2=="NO":
                                nom2="N/A"
                            nom3=input("Ingrese el nombre y apellido de la madre (Si no es presente ponga NO)\n").upper()
                            if nom3=="NO":
                                nom3="N/A"
                                os.system('cls')
                            rut1=input("Ingrese el rut del padre (Si no es presente ponga 0)\n")
                            if rut1=="0":
                                rut1="N/A"
                            rut2=input("Ingrese el rut de la madre (Si no es presente ponga 0)\n")
                            if rut2=="0":
                                rut2="N/A"
                                os.system('cls')
                            pais1=input("Ingrese nacionalidad del padre (Si no es presente ponga NO)\n").upper()
                            if pais1=="NO":
                                pais1="N/A"
                            pais2=input("Ingrese nacionalidad de la madre (Si no es presente ponga NO)\n").upper()
                            if pais2=="NO":
                                pais2="N/A"
                                os.system('cls')
                            resp2=input(f"Los datos ingresados son:\nNombre del recien nacido:\n{bebe1}{bebe1}\nNombre de los padres:\n{nom2}\n{nom3}\nRut de los padres:\n{rut1}\n{rut2}\nNacionalidad de los padres:\n{pais1}\n{pais2}\n¿Son correctos estos datos?[SI/NO]").upper()
                            while resp2 not in ["SI", "NO"]:
                                os.system('cls')
                                print("ERROR, seleccione una opcion valida [SI/NO]")
                            resp=input(f"El nombre(s) es {bebe1} {bebe2} ¿Es correcto?[SI/NO]\n").upper()
                            if resp2== "SI":
                                print(f"Incripcion completa\n Este tramite no tiene costo\nLos datos ingresados les seran enviados al correo ({correo})\nSi quiere ir a retirar el certificado fisico por correo se le será asignado un numero de atencion")
                                total_gente + 1
                            elif resp2=="NO":
                                print("Volviendo a ingresar datos...")
                                time.sleep(1)
                        elif resp=="NO":
                            print("Volviendo a ingresar datos...")
                            time.sleep(1)
                    elif nacimiento=="NO":
                        print("Saliendo...")
                        time.sleep(1)
                        break
                    os.system('cls')
            return gente
        sistema()
        gente=sistema()
total_gente()
print("Funciona")