# super mercado 

from os import system
import time

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

def menu_1():
    print("""
---Super mercado---
          
1.- Comprar
2.- Salir
""")
    op=validacion("Seleccione una opcion:\n", "Seleccione una opcion valida", range(1,3))
    return op

def sistema(op):
    while True:
        match op:
            case 1:
                super()
            case 2:
                exit

def super():
    print("""
--- ¿Que desea llevar? ---
          
1.- Coca Cola 1.75L         $1250
2.- Lays 200gr              $2190
3.- Pan (2kg)               $1790
4.- Salir y Pagar
5.- Anular Compra
""")
    op1=validacion("Seleccione una opcion:\n", "Seleccione una opcion valida", range(1,6))
    return op1

def sistema_2(op1):
    prod1 = 0
    prod2 = 0
    prod3 = 0

    while True:
        match op1:
            case 1:
                print(f"Usted lleva {1+prod1} Coca Cola")
            case 2:
                print(f"Usted lleva {1+prod2} Lays")
            case 3:
                print(f"Usted lleva {1+prod3} Pan")
            case 4:
                prodTotal=prod1+prod2+prod3
                break
                boleta()
            case 5:
                break

    return prodTotal

def boleta(prodTotal):
    nom=input("Ingrese su nombre:\n")
    print(f"""
""")

if __name__ == "__main__":
    opcion_menu = menu_1()
    sistema(opcion_menu)
    opcion_menu2 = super()
    sistema_2(opcion_menu2)