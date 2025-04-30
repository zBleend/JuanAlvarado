# La florida 20%, la pintana 30%, puente alto 25%, san joaquin 15%
# El arancel actual es de 200000 por semestre
# grupo familiar 1 persona 2%, 2 a 4 personas 3%, 5 o más personas 4%
# Preguntar al usuario en qué comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200000 por semestre
# Basados en las respuestas del usuario y en la informacion dada, calcular su descuento

import time
from os import system

def limpiar_pantalla():
    system('cls||clear')

def menu_comuna():
    try:
        while True:
            com=int(input("""¿En qué comuna vives? [1/4]
1.- La Florida
2.- La Pintana
3.- Puente Alto
4.- San Joaquín
"""))
            if com == 1:
                descuentoComuna = 20
                return com, descuentoComuna
            elif com == 2:
                descuentoComuna = 30
                return com, descuentoComuna
            elif com == 3:
                descuentoComuna = 25
                return com, descuentoComuna
            elif com == 4:
                descuentoComuna = 15
                return com, descuentoComuna
            else:
                print("Error: Debe ingresar una opcion valida.")
                time.sleep(1)
                limpiar_pantalla()
                continue
    except ValueError:
        print("Error: Debe ingresar una opcion valida.")
        time.sleep(1)
        limpiar_pantalla()
        return menu_comuna

def menu_personas():
    try:
        while True:
            personas=int(input("""
¿Con cuantas personas vives? [1/5]
1.- 1 persona
2.- 2 personas
3.- 3 personas
4.- 4 personas
5.- 5 personas o más                       
"""))
            if personas == 1:
                descuentoPersona = 2
                return personas, descuentoPersona
            elif personas >= 2 and personas <= 4:
                descuentoPersona = 3
                return personas, descuentoPersona
            elif personas == 5:
                descuentoPersona = 4
                return personas, descuentoPersona
            else:
                print("Error: Debe ingresar una opcion valida.")
                time.sleep(1)
                limpiar_pantalla()
                continue
    except ValueError:
        print("Error: Debe ingresar una opcion valida.")
        time.sleep(1)
        limpiar_pantalla()
        return menu_personas

def calculadora(descuentoComuna, descuentoPersona):
    arancel = 200000
    descuentoTotal = (descuentoComuna + descuentoPersona) / 100
    arancelDescuento = arancel * descuentoTotal
    return descuentoTotal, arancelDescuento, arancel

def sistema_final(arancel, descuentoTotal, personas, com, descuentoComuna, descuentoPersona, arancelDescuento):
    arancelFinal = arancel - arancelDescuento
    print(f"Su comuna es {com}")
    print(f"Tiene un descuento de {descuentoComuna}% por vivir en esa comuna")
    print(f"Tiene un descuento de {descuentoPersona}% por vivir con {personas} personas")
    print(f"El descuento total es de: {descuentoTotal * 100}%")
    print(f"El arancel actual es de: {arancel}")
    print(f"El arancel final es de: {arancelFinal}")
    return arancelFinal

if __name__ == "__main__":
    limpiar_pantalla()
    print("Bienvenido al sistema de descuentos")
    com, descuentoComuna = menu_comuna()
    personas, descuentoPersona = menu_personas()
    descuentoTotal, arancelDescuento, arancel = calculadora(descuentoComuna, descuentoPersona)
    sistema_final(com, descuentoComuna, personas, descuentoPersona, descuentoTotal, arancelDescuento, arancel)