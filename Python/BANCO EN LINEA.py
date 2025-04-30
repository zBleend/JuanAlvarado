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
------Banco en línea------

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
            if var.isdigit() and int(var) in rango:
                var=int(var)
                return (var)
            else:
                print(mensaje_error)
    except (ValueError, NameError):
        print(mensaje_error)

def sistema(op, usuario_registrado, saldos_usuarios, billetes):
    if op==1:
        user = inicio_sesion(usuario_registrado)
        if user:
            while True:
                op2 = menu_cajero(user)
                if sistema_cajero(op2, user, saldos_usuarios, billetes) == "salir":
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
3.- Retirar dinero
4.- Salir
""")
    return validacion("Seleccione una opcion: ", "Seleccione una opcion valida [1,4]", range(1,5))

def sistema_cajero(op2, user, usuario_registrado, saldos_usuarios, billetes):
    if op2==1:
        print(f"Su saldo actual es de: ${saldos_usuarios[user]}")
        input("\nPresione Enter para continuar...")
        return "continuar"
    elif op2==2:
        transferir(user, saldos_usuarios, usuario_registrado)
        return "continuar"
    elif op2==3:
        retiro(user, saldos_usuarios, billetes)
        return "continuar"
    elif op2==4:
        print("Cerrando sesion...")
        time.sleep(1.5)
        limpiar_pantalla()
        return "salir"

def transferir(user, saldos_usuarios, usuario_registrado):
    limpiar_pantalla()
    destinatario=input(f"""
------Trasferir------   
Saldo actual: {saldos_usuarios[user]}
Ingrese el nombre del destinatario: 
""")

    if destinatario not in usuario_registrado:
        print("\nError: El destinatario no existe")
        time.sleep(1)
        return

    if destinatario == user:
        print("Error: No puedes trasferirte a ti mismo")
        time.sleep(1)
        return

    while True:
        try:
            monto=int(input("\nIngresa el monto a trasferir:            (Minimo $500)\n$"))
            if monto< 500:
                print("El monto tiene que ser como minimo arriba de $500")
                continue
            if monto>saldos_usuarios[user]:
                print("Fondos insuficientes")
                continue
            print(f"\n¿Desea transferir ${monto} a {destinatario}?")
            conf=input("""
1.- Si
2.- No""")
            if conf=="1":
                saldos_usuarios[user] -= monto
                saldos_usuarios[destinatario] += monto
                input(f"""
Trasferencia exitosa
Nuevo saldo: ${saldos_usuarios[user]}
Preciones Enter para continuar...
""")
                return
            elif conf=="2":
                print("\nTrasferencia cancelada")
                time.sleep(1)
                return
        except ValueError:
            print("Ingrese un monto valido")

def retiro(user, saldo_usuarios, billetes):
    limpiar_pantalla()
    print(f"""
------Retiro de efectivo------
Tu saldo actual es de: ${saldo_usuarios[user]}
Billetes disponibles: $5.000 | $10.000 | $15.000 | $20.000 |
""")
    while True:
        try:
            monto=int(input("\nIngresa el monto a retirar:            (Minimo $5.000)\n$"))
            if monto <= 5000:
                print("Error: El minimo a retirar es $5.000")
                continue
            if monto > saldo_usuarios[user]:
                print("Error: Fondos insuficientes")
                continue
            if not es_monto_valido(monto, billetes):
                print("Error: El monto debe ser múltiplo de $5.000")
                continue
            if realizar_retiro(monto, billetes):
                saldo_usuarios[user] -= monto
                input(f"""
Retiro exitoso
Nuevo saldo: ${saldo_usuarios[user]}
Presione Enter para continuar...
""")
                return
            else:
                print("No hay suficientes billetes para este monto")
        except ValueError:
            print("Ingrese un monto valido")

def es_monto_valido(monto, billetes):
    return monto % 5000 == 0

def realizar_retiro(monto, billetes):
    temp_billetes=billetes.copy()
    denominaciones = sorted(temp_billetes.keys(), reverse=True)
    for denom in denominaciones:
        if monto >= denom:
            cant= min(monto//denom, temp_billetes[denom])
            monto -= denom*cant
            temp_billetes[denom] -= cant
    if monto == 0: 
        for denom in billetes:
            billetes[denom] = temp_billetes[denom]
        return True
    return False

def registro(usuario_registrado, saldos_usuarios):
    print("------Registro------")
    while True:
        user=input("Ingrese su nombre de usuario para registrarse: \n").strip()
        if user in usuario_registrado:
            print("Error, este nombre ya fue registrado") 
            continue
        elif not user.strip():
            print("Error: El nombre no puede estar vacío")
        else:
            break
    clave_user=clave()
    saldo_inicial = random.choice([5000, 10000, 15000, 20000])
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
    usuario_registrado ={}
    saldos_usuarios ={}
    billetes ={
        20000:30,
        15000:30,
        10000:30,
        5000:30
    }
    return usuario_registrado, saldos_usuarios, billetes

if __name__=="__main__":
    usuario_registrado, saldos_usuarios, billetes = registos()
    while True:

        op=menu()
        sistema(op, usuario_registrado, saldos_usuarios, billetes)
        if op != 3:
            limpiar_pantalla()