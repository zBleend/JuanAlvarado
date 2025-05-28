import time
from os import system

def limpiar_pantalla():
    system('cls||clear')

def banner1():
    print("*************************")
    print("-----Lavado de autos-----")
    print("*************************")

def pagos(totalventas):
    while True:
        try:
            op1 = int(input("""
Seleccione tipo de lavado:
1.- Full $15.000
2.- Standar $10.000
3.- Basico $7.000
4.- Cancelar
"""))
        except (Exception, ValueError):
            print("Error, Ingresa una opcion valida")
        if op1 == 1:
            totalventas += 15000
            print("Usted seleccionó Lavado Full")
            time.sleep(1)
            limpiar_pantalla()
        elif op1 == 2:
            totalventas += 10000
            print("Usted seleccionó Lavado Standar")
        elif op1 == 3:
            totalventas += 7000
            print("Usted seleccionó Lavado Basico") 
        elif op1 == 4:
            print("Adios")
            time.sleep(1)
            limpiar_pantalla()
            return totalventas
        time.sleep(1)
        limpiar_pantalla()
        return totalventas

def ventas(totalventas):
    clave = "3366"
    try:
        clave1 = input("Ingrese contraseña para ver ventas:\n")
    except (Exception, ValueError):
        print("Error, Ingrese un dato valido")
        if clave1 == clave:
            print(f"El Total de ventas es {totalventas}")
            input("Presione enter para salir")
            limpiar_pantalla()
        else:
            print("Clave erronea")
            time.sleep(1)
            limpiar_pantalla()
    

def menu():
    totalventas = 0
    while True:
        banner1()
        time.sleep(1)
        try:
            op = int(input("""
1.- Cursar pago del lavado
2.- Ver ventas diarias
3.- Salir
"""))
        except (Exception, ValueError):
            print("Error: Ingrese una opcion valida")
        if op == 1:
            totalventas = pagos(totalventas)
        elif op == 2:
            ventas(totalventas)
        elif op == 3:
            break
menu()