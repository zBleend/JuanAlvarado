def menu():
    nombres = []
    apellidos = []
    while True:
        try:
            op = int(input("""--- Bienvenido ---
1.- Ingresar nombres
2.- Ingresar apellidos
3.- Ver nombres y apellidos
4.- Salir
"""))
            match op:
                case 1:
                    nombres = op1(nombres)
                case 2:
                    apellidos = op2(apellidos)
                case 3:
                    op3(nombres, apellidos)
                case 4:
                    print("--- Adios ---")
                    break
                case _:
                    print("Seleccione una opcion valida")    
        except Exception:
            print("Seleccione una opcion valida")


def op1(nombres):
    while True:
        nombre = input("Ingrese nombres:\n")
        if nombre.lower() == "salir":
            return nombres
        else:
            nombres.append(nombre)

def op2(apellidos):
    while True:
        apellido = input("Ingrese apellidos:\n")
        if apellido.lower() == "salir":
            return apellidos
        else:
            apellidos.append(apellido)

def op3(nombres, apellidos):
    c = 0
    for i in nombres:
        print(nombres[c], apellidos[c])
        c += 1

menu()