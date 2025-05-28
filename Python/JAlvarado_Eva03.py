# Ejercicio 1

import time
from os import system

# def limpiar_pantalla():
#     system('cls||clear')

# def menu():
#     años1 = 0
#     años2 = 0
#     años = 0

#     empleados = int(input("Ingrese la cantidad de empleados a registrar:\n"))
#     for i in range(empleados):
#         nombre = input("Ingrese el nombre del empleado:\n")
#         while True:
#             try:
#                 años = int(input("Ingrese los años de antiguedad del empleado:\n"))
#                 if años <= 10:
#                     print("Tiene 10 o menos años de antigüedad")
#                     años1 += 1
#                     time.sleep(1.5)
#                     limpiar_pantalla()
#                     break
#                 elif años > 10:
#                     print("Tiene mas de 10 años de antigüedad")
#                     años2 += 1
#                     time.sleep(1.5)
#                     limpiar_pantalla()
#                     break
#             except (ValueError, Exception):
#                 print("Debe ingresar un numero entero")
#         print("Cargando...")
#         time.sleep(1)
#         limpiar_pantalla()
#         print(f"Se registraron {años2} con más de 10 años de antigüedad")
#         print(f"Se registraron {años1} con 10 o menos años de antigüedad")

# menu()

# ==========================================================================================================
# Ejercicio 2  No logré que se pudiera restar la cantidad de entradas
# ==========================================================================================================

entradas = 50

def comprar(entradas):
    if entradas <= 0:
        print("Lo sentimos se acabaron las entradas")
    else:
        while True:
            try:
                op = int(input("¿Cuantas entradas quiere comprar?\n"))
                if op > entradas:
                    print("Lo sentimos, excede el limite de entradas disponibles")
                else:
                    entradas -= op
                    print(f"Compra exitosa. Quedan {entradas} entradas.")
                    return entradas
            except (ValueError, Exception):
                print("Debe ingresar un numero entero valido")
                
def menu(entradas):
    while True:
        try:
            op = int(input("""***** Cine Estrella *****
Bienvenido al sistema de venta de entradas del Cine Estrella
1.	Ver cuántas entradas quedan.
2.	Comprar una cantidad de entradas.
3.	Salir del sistema.
"""))
            if op == 1:
                limpiar_pantalla()
                entrada(entradas)
            elif op == 2:
                limpiar_pantalla()
                entradas = comprar(entradas)
            elif op == 3:
                limpiar_pantalla()
                print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
                break
        except (ValueError, Exception):
            print("Error, Seleccione una opcion valida (1-3)")

def limpiar_pantalla():
    system('cls||clear')
    
def entrada(entradas):
    limpiar_pantalla()
    print(f"Quedan {entradas} disponibles actualmente")
    time.sleep(1.5)
    limpiar_pantalla()

menu(entradas)
