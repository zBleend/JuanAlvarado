from os import system
import time

def menu():
    while True:
        try:
            op = int(input("""=============================
|         BIENVENIDO        |
=============================

=============================
| 1. Ingresar Nota          |
| 2. Borrar Nota            |
| 3. Mostrar Notas          |
| 4. Sacar Promedio         |
| 5. Limpiar Todas las notas|
| 6. Salir                  |
=============================
"""))
            if 1 <= op <= 6:
                return op
            else:
                print("Seleccione una opcion valida") 
        except Exception:
            print("Error, Seleccione una opciona valida")
        


def opciones():
    notas = []
    while True:
        op = menu()
        match op:
            case 1:
                notas = ingresar_nota(notas)
            case 2:
                notas = borrar_nota(notas)
            case 3:
                notas = mostrar_notas(notas)
            case 4:
                notas = sacar_promedio(notas)
            case 5:
                if notas:
                    notas.clear()
                    print("Se han borrado todas las notas")
                else:
                    print("No hay notas para borrar")
                time.sleep(1.5)
            case 6:
                print("Saliendo del programa")
                time.sleep(1)
                break

def ingresar_nota(notas):
    try:
        nota = float(input("Ingrese la nota:\n"))
        notas.append(nota)
        print("Nota ingresada")
        time.sleep(0.8)
    except ValueError:
        print("Error, ingrese un valor válido")
    return notas

def borrar_nota(notas):
    while True:
        if notas:
            try:
                nota_a_borrar = float(input("Ingrese la nota a borrar:\n"))
                if nota_a_borrar in notas:
                    notas.remove(nota_a_borrar)
                    print(f"Nota {nota_a_borrar} eliminada correctamente.")
                    time.sleep(1.5)
                    return notas
                else:
                    print("La nota no está en la lista. Verifique el número ingresado.")
                    time.sleep(1.5)
            except ValueError:
                print("Error, ingrese un número válido.")
                time.sleep(1)
        else:
            print("No hay notas para borrar.")
            time.sleep(1.5)
            return notas

def mostrar_notas(notas):
    if notas:
        print("Notas ingresadas:")
        for n in notas:
            print(n)
    else:
        print("No hay notas para mostrar")
    input("Pulse enter para continuar")

def sacar_promedio(notas):
    if notas:
        promedio = sum(notas) / len(notas)
        print(f"El promedio de las notas es: {promedio:.2f}")
        print("La nota mas alta fue: ", max(notas))
        print("La nota mas baja fue: ", min(notas))
        input("Presione enter para salir...")
    else:
        print("No hay notas para calcular el promedio.")
        time.sleep(1)

opciones()