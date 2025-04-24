import os
import platform
import time
def banner1():
    print("*************************************")
    print("--------Bienvenido al sistema--------")
    print("*************************************")

def banner2():
    print("*************************************")
    print("----------------Adios----------------")
    print("*************************************")


def limpiar_pantalla():
    if platform.system()=="Windows":
        os.system('cls')
    else:
        os.system('clear')

def inicio_de_sesion():
    banner1()
    clave="3322"
    intento=3
    resp=input(f"Ingrese su clave: \nTienes {intento} intentos\n")
    while True:
        if clave==resp:
            limpiar_pantalla()
            print("Bienvenido al sistema...")
            break
        intento-=1
        if intento==0:
            limpiar_pantalla()
            print("Demasiados intentos, saliendo del sistema...")
            time.sleep(1)
            limpiar_pantalla()
            banner2()
            break
        else:
            limpiar_pantalla()
            banner1()
            print(f"Clave incorrecta tienes {intento} intentos")
            resp=input("Ingrese su clave: ")
inicio_de_sesion()