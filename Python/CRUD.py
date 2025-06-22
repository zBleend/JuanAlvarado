# Crear programa CRUD (create, read, update, delete) del siguiente diccionario

personas = {
    1 : {"Nombre" : "Juan Abrigo",
         "Numeros" : [12345678],
         "Estado_Civil" : "Soltero",
         "Trabajando" : True,
         "Edad" : 22},

    2 : {"Nombre" : "Benja Cespedes",
         "Numeros" : [23456789],
         "Estado_Civil" : "Casado",
         "Trabajando" : True,
         "Edad" : 22}
}

def menu():
    while True:
        try:
            op = int(input("""=== Bienvenido ===
1.- Ingresar Usuario
2.- Ver estado de Usuario
3.- Editar Usuario
4.- Borrar Usuario
5.- Salir
"""))
            if op not in [1, 2, 3, 4]:
                print("Seleccione una opcion valida")
            elif op == 5:
                print("Adios...")
                break
            else:
                return op
        except Exception as e:
            print("Error al ingresar los datos. Intente nuevamente. Detalle:", e)

def ingresar_usuario():
    while True:
        try:
            nombre = input("Ingrese nombre de usuario:\n")
            numero = int(input("Ingrese su numero:\n"))
            estado_civil = input("Ingrese su estado civil: [Casado/Soltero]\n")
            while True:
                trabajando_input = input("¿Está trabajando?: [SI/NO]\n").lower()
                if trabajando_input == "si":
                    trabajando = True
                    break
                elif trabajando_input == "no":
                    trabajando = False
                    break
                else:
                    print("Seleccione una opcion valida")
            edad = int(input("Ingrese su Edad:\n"))
            nuevo_id = max(personas.keys(), default=0) + 1
            personas[nuevo_id] = {
            "Nombre" : nombre,
            "Numeros" : numero,
            "Estado_Civil" : estado_civil,
            "Trabajando" : trabajando,
            "Edad" : edad
        }
            print("Usuario ingresado correctamente")
            return False
        except Exception as e:
            print("Error al ingresar los datos. Intente nuevamente. Detalle:", e)

def estado_usuario():
    nombre = input("Ingrese el nombre del usuario para buscar:\n")
    encontrado = False
    for d in personas.values():
        if d["Nombre"].lower() == nombre.lower():
            print("Estado del usuario:")
            for c, v in d.items():
                print(f"f{c}: {v}")
            encontrado = True
            break
    if not encontrado:
        print("Usuario no registrado")

def actualizar_usuario():
    nombre = input("Ingrese el nombre del usuario para buscar:\n")
    encontrado = False
    for d in personas.values():
        if d["Nombre"].lower() == nombre.lower():
            print("Estado del usuario:")
            for c, v in d.items():
                print(f"f{c}: {v}")
            encontrado = True
            break
    if not encontrado:
        print("Usuario no registrado")

def borrar_usuario():
    try:
        borrar = int(input("Ingrese el ID del usuario que desea borrar:\n"))
        if borrar in personas:
            del personas[borrar]
            print("Usuario borrado correctamente")
        else:
            print("El usuario con ese ID no existe.")
    except Exception as e:
        print("Error al borrar el usuario. Detalle:", e)

def sistema():
    op = menu()
    while True:
        match op:
            case 1:
                ingresar_usuario()
            case 2:
                estado_usuario()
            case 3:
                actualizar_usuario()
            case 4:
                borrar_usuario()

sistema()