# BANCO

from os import system
import time
import random

def limpiar_pantalla():
    system('cls||clear')

def banner1():
    print("*************************************")
    print("----Bienvenido al Banco en linea-----")
    print("*************************************")

def banner2():
    print("*************************************")
    print("----------------Adios----------------")
    print("*************************************")

def menu():
    banner1()
    print("Cargando...")
    time.sleep(2)
    limpiar_pantalla()
    print("""
Banco en linea

1.- Iniciar sesion
2.- Registrarse
3.- Salir
        """)
    op=validacion("Seleccione una opcion: ", "Seleccione una opcion valida [1,3]", range(1,4))
    return op

def validacion(mensaje, mensaje_error, rango):
    try:
        while True:
            var=input(mensaje)
            if var.isdigit and int(var) in rango:
                var=int(var)
                return (var)
            else:
                print(mensaje_error)
    except ValueError or NameError:
        print(mensaje_error)

def sistema(op):
    if op==1:
        print("Funciona 1")
    elif op==2:
        print("Funciona 2")
        registro()
    elif op==3:
        limpiar_pantalla()
        banner2()
        exit()

def inicio_sesion():
    input("Ingrese su nombre de usuario")


def registro(usuario_registrado, saldos_usuarios):
    user=input("Ingrese su nombre de usuario para registrarse: \n")
    if user in usuario_registrado:
        print("Error, este nombre ya fue registrado") 
        return None
    
def validar_clave(clave):
    if len(clave) < 8:
        return False, "La clave debe tener un minimo de 8 caracteres"
    if not any(caracter.isdigit() for caracter in clave):
        return False, "La clave debe tener al menos un número"
    return True, "Contraseña válida"

def clave():
    while True:
        clave_user=input("Ingrese una clave: \n")
        es_valida, mensaje = validar_clave(clave_user)
        if es_valida:
            return clave_user
        else:
            print(f"Error {mensaje}. Intente nuevamente")

def registos():
    usuario_registrado={}
    saldos_usuarios={}
    return usuario_registrado, saldos_usuarios


if __name__=="__main__":
    op = menu()
    op= sistema(op)
    