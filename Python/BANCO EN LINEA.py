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

def sistema(op, usuario_registrado, saldos_usuarios):
    if op==1:
        # inicio_sesion(usuario_registrado)
        user = inicio_sesion(usuario_registrado)
        if user:
            while True:
                op2 = menu_cajero(user)
                if sistema_cajero(op2, user, saldos_usuarios) == "salir":
                    break
    elif op==2:
        registro(usuario_registrado, saldos_usuarios)
    elif op==3:
        limpiar_pantalla()
        banner2()
        exit()

def inicio_sesion(usuario_registrado):
    print("------Inicio de sesión------")
    user=input("Ingrese su nombre de usuario:\n")

    if user not in usuario_registrado:
        print("Error: Nombre de usuario no registrado\n")
        time.sleep(1)
        return None
    clave=input("Ingrese contraseña:\n")
    if usuario_registrado[user] == clave:
        limpiar_pantalla()
        print("Cargando...")
        time.sleep(2)
        limpiar_pantalla()
        return user
    else:
        print("Error, clave incorrecta")
        time.sleep(1)
        return None

def menu_cajero(user):
    limpiar_pantalla()
    print(f"Bienvenido {user}\n")
    print("""
1.- Ver saldo
2.- Transferir
3.- Salir
""")
    return validacion("Seleccione una opcion: ", "Seleccione una opcion valida [1,3]", range(1,4))

def sistema_cajero(op2, user, saldos_usuarios):
    if op2==1:
        print(f"Su saldo actual es de: ${saldos_usuarios[user]}")
        input("\nPrecione Enter para continuar...")
        return "continuar"
    elif op2==2:
        print("Aun en desarrollo")
        time.sleep(1)
        return "continuar"
    elif op2==3:
        print("Cerrando sesion...")
        time.sleep(1)
        limpiar_pantalla()
        return "Salir"

def registro(usuario_registrado, saldos_usuarios):
    print("------Registro------")
    user=input("Ingrese su nombre de usuario para registrarse: \n")
    if user in usuario_registrado:
        print("Error, este nombre ya fue registrado") 
        return None
    clave_user=clave()
    saldo_inicial = random.choice([5000, 10000, 20000])

    usuario_registrado[user] = clave_user
    saldos_usuarios[user] = saldo_inicial

    print("El registro fue exitoso")
    return user
    
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
    usuario_registrado, saldos_usuarios = registos()
    op=menu()
    op=sistema(op, usuario_registrado, saldos_usuarios)