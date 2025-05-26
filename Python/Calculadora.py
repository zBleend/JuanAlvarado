import os

def suma():
    try:
        print("Suma de numeros")
        num1=int(input("Ingresa un numero\n"))
        num2=int(input("Ingrese otro numero: \n"))
        resultado=num1+num2
        print(f"{num1} + {num2} = {resultado}")
    except(ValueError):
        print("Error")

def resta():
    try:
        print("Resta de numeros")
        num1=int(input("Ingresa un numero\n"))
        num2=int(input("Ingrese otro numero: \n"))
        resultado=num1-num2
        print(f"{num1} - {num2} = {resultado}")
    except(ValueError):
        print("Error")
def multi():
    try:
        print("Multipliacion de numeros")
        num1=int(input("Ingresa un numero\n"))
        num2=int(input("Ingrese otro numero: \n"))
        resultado=num1*num2
        print(f"{num1} x {num2} = {resultado}")
    except(ValueError):
        print("Error")

def divi():
    try:
        print("Division de numeros")
        num1=int(input("Ingresa un numero\n"))
        num2=int(input("Ingrese otro numero: \n"))
        resultado=num1/num2
        print(f"{num1} ÷ {num2} = {resultado}")
    except(ValueError):
        print("Error")


def calc():
    try:
        while True:
            op=int(input("""Calculadora
Seleccione una opcion
1.- Suma
2.- Resta
3.- Multiplicacion
4.- Division
5.- Salir
"""))
            match op:
                case 1:
                    suma()
                case 2:
                    resta()
                case 3:
                    multi()
                case 4:
                    divi()
                case 5:
                    os.system('cls')
                    print("Adios")
                    break
                case _:
                    print("Opcion no valida")
    except (ValueError, NameError):
        print("Error")


calc()