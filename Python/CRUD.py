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
            if op not in [1, 2, 3, 4, 5]:
                print("Seleccione una opcion valida")
            else:
                return op
        except Exception as e:
            print("Error al ingresar los datos. Intente nuevamente. Detalle:", e)

def ingresar_usuario():
    try:
        nombre = input("Ingrese nombre de usuario:\n")
        numero = int(input("Ingrese su numero:\n"))
        estado_civil = input("Ingrese su estado civil: [Casado/Soltero]\n")
        trabajando = input("¿Está trabajando?: [SI/NO]\n")
        if trabajando == "si":
            trabajando = True
        elif trabajando == "no":
            trabajando = False
        else:
            print("Seleccione una opcion valida")
        edad = int(input("Ingrese su Edad:\n"))
        nuevo_id = len(personas)
        personas[nuevo_id + 1] = {
        "Nombre" : nombre,
        "Numeros" : numero,
        "Estado_Civil" : estado_civil,
        "Trabajando" : trabajando,
        "Edad" : edad
    }
        print("Usuario ingresado correctamente")
    except Exception as e:
        print("Error al ingresar los datos. Intente nuevamente. Detalle:", e)

def borrar_usuario():
    borrar = int(input("Seleccione lo que quiere borrar:\n"))
    del 
def sistema():
    op = menu()
    match op:
        case 1:
            ingresar_usuario()

menu()