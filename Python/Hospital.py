import time
from os import system

def Limpieza ():
    system('cls')

def Sistema_bienvenida():
    print("""
*****************************
    Bienvenido al sistema
*****************************
        """)
    time.sleep(2)
    Limpieza()

def validacion(mensaje, mensaje_mal, rango):
    try:
        while True:
            var=input(mensaje)
            if var.isdigit and int(var) in rango:
                var=int(var)
                return var
            else:
                print(mensaje_mal)
    except ValueError or NameError:
        print(mensaje_mal)

def Menu():
    print("""
1.- Ingresar paciente
2.- Ver diagnostico
3.- Borrar paciente
4.- Salir\n""")
    op=validacion("Seleccione una opcion: ", "Seleccione una opcion valida [1,4]", range(1,5))

if __name__ == "__main__":
    Sistema_bienvenida()
    Menu()