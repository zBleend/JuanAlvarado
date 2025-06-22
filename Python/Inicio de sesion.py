usuarios = {
    1 : {
        "Nombre" : "Juan",
        "Contraseña" : "Leon2022"
         },
    2 : {
        "Nombre" : "Alejandro",
        "Contraseña" : "Satanico123"
    }
}

def registro():
    nombre = input("Ingrese su nombre de usuario:\n")
    contraseña = input("Ingrese su contraseña:\n")
    nuevo_id = max(usuarios.keys(), default=0) + 1
    usuarios[nuevo_id] = {
        "Nombre" : nombre,
        "Contraseña" : contraseña
    }
    print("Registro exitoso")

def inicio():
    user = input("Ingrese su usuario:\n")
    clave = input("Ingrese su clave:\n")
    encontrado = False
    for d in usuarios.values():
        if d["Nombre"] == user and d ["Contraseña"] == clave:
            encontrado = True
            break
    if encontrado == True:
        print("Bienvenido")
    else:
        print("Error, usuario o clave incorrecta")

while True:
    try:
        op = int(input("""--- Bienvenido ---
1.- Iniciar Sesion
2.- Registrarse
3.- Ver usuarios
4.- Salir
"""))
    except Exception as e:
        print("Seleccione una opcion valida", e)

    match op:
        case 1:
            inicio()
        case 2:
            registro()
        case 3:
            for u, c in usuarios.items():
                print(f"ID: {u} | Usuario: {c['Nombre']} | Contraseña: {c['Contraseña']}")
        case 4:
            print("Adios")
            break

