prod = {
    1 : {
        "Nombre" : "Zelda Totk",
        "Precio" : 80000,
        "Code" : "ZZtt124"
    },
    2 : {
        "Nombre" : "Zelda Botw",
        "Precio" : 80000,
        "Code" : "ZZbb132"
    }
}

def menu():
    try:
        op = int(input("""
1.- Registrar un juego
2.- Mostrar juegos
3.- Actualizar juego
4.- Borrar Juego
5.- Salir
"""))
        return op
    except Exception as e:
            print("Error: ", e)

def registro():
    while True:
        try:
            nombre = input("Ingrese el nombre del producto:\n")
            precio = int(input("Ingrese el precio:\n"))
            code = input("Ingrese el codigo del productor:\n")
            if validar_code(code) == True and validar_precio(precio) == True and validar_nombre(nombre) == True:
                nuevo_id = max(prod.keys(), default=0) + 1
                prod[nuevo_id] = {
                "Nombre" : nombre,
                "Precio" : precio,
                "Code" : code
            }
                print("Registro exitoso")
                return sistema()
            else:
                print("Error, codigo invalido")
        except Exception as e:
            print("Error: ", e)

def validar_nombre(nombre):
    if len(nombre) < 2:
        print("El nombre del producto tiene que tener 2 caracteres")
    else:
        return True

def validar_precio(precio):
    if precio < 8000 or precio > 100000:
        print("Error, el precio no es correcto [Entre 8.000 y 100.000]")
    else:
        return True

def validar_code(code):
    if len(code) < 7:
        print("El codigo tiene que tener un minimo de 7 caracteres")
    elif sum(1 for c in code if c.islower()) != 2:
        print("La clave debe de tener al menos 2 letras minusculas")
    elif sum(1 for c in code if c.isupper()) != 2:
        print("La clave debe de tener al menos 2 letras mayúsculas")
    elif sum(1 for c in code if c.isdigit()) != 3:
        print("La clave debe de tener 3 numeros")
    else:
        return True

def actualizar_juego():
    try:
        id_juego = int(input("Ingrese la ID del juego que quiere actualizar:\n"))
        if id_juego not in prod:
            print("ID no encontrada.")
            return
        juego = prod[id_juego]
        print(f"Datos actuales: Nombre: {juego['Nombre']}, Precio: {juego['Precio']}, Code: {juego['Code']}")
        campo = input("¿Qué desea actualizar? (nombre/precio/code): ").lower()
        if campo == "nombre":
            nuevo_nombre = input("Ingrese el nuevo nombre:\n")
            if validar_nombre(nuevo_nombre) == True:
                juego["Nombre"] = nuevo_nombre
                print("Nombre actualizado.")
        elif campo == "precio":
            nuevo_precio = int(input("Ingrese el nuevo precio:\n"))
            if validar_precio(nuevo_precio) == True:
                juego["Precio"] = nuevo_precio
                print("Precio actualizado.")
        elif campo == "code":
            nuevo_code = input("Ingrese el nuevo código:\n")
            if validar_code(nuevo_code) == True:
                juego["Code"] = nuevo_code
                print("Código actualizado.")
        else:
            print("Campo no válido.")
    except Exception as e:
        print("Error al actualizar:", e)

def sistema():
    while True:
        op = menu()
        match op:
            case 1:
                registro()
            case 2:
                for k, v in prod.items():
                    print(f'ID {k}, Nombre {v["Nombre"]}, Precio {v["Precio"]}, Code {v["Code"]}')
                input("Presione enter para continuar")
                return sistema()
            case 3:
                actualizar_juego()
            case 4:
                try:
                    borrar = int(input("Ingrese la ID del juego que quiere borrar:\n"))
                    del prod[borrar]
                    return sistema()
                except Exception:
                    print("Elije una ID valida")
            case 5:
                print("Adios")
                break
            case _:
                print("Seleccione una opcion valida")

sistema()