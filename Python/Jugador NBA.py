nba = {
    1 : {
        "Nombre" : "Lebron James",
        "Precio" : 1000,
        "Equipo" : "Miami heat"
    },
    2 : {
        "Nombre" : "Stephen Curry",
        "Precio" : 2000,
        "Equipo" : "Lakers"
    }
}

while True:
    try:
        op = int(input("""
1.- Ver jugadores
2.- Actualizar datos jugador
3.- Añadir Jugador
4.- Borrar jugador
5.- Salir
"""))
        match op:
            case 1:
                for k, v in nba.items():
                    print(f"ID: {k} Nombre: {v['Nombre']} Precio: {v['Precio']} Equipo: {v['Equipo']}")
                input("Pulsa enter para continuar")
            case 2:
                user_id = int(input("Ingrese la ID del jugado que quiere modificar:\n"))
                if user_id not in nba:
                    print("Esa ID no está registrada")
                else:
                    v = nba[user_id]
                    print("Datos actuales del ID")
                    print(f"Nombre: {v['Nombre']}, Precio: {v['Precio']}, Equipo: {v['Equipo']}")
                    jugador = input("¿Que vas a cambiar [Nombre, Precio, Equipo]\n").lower()
                    if jugador == "nombre":
                        nom_jugador = input("Ingrese el cambio:\n")
                        v["Nombre"] = nom_jugador
                    elif jugador == "precio":
                        precio_jugador = input("Ingrese el cambio:\n")
                        v["Precio"] = precio_jugador
                    elif jugador == "equipo":
                        equi_jugador = input("Ingrese el cambio:\n")
                        v["Equipo"] = equi_jugador
                    else:
                        print("Error, elige algo valido")
                    input("Listo, cambiaste algo, xd")
            case 3:
                nombre = input("Ingresa el nombre del jugador:\n")
                precio = int(input("Ingresa el precio del jugador:\n"))
                equipo = input("Ingresa el equipo del jugador:\n")
                nuevo_id = max(nba.keys(), default=0) + 1
                nba[nuevo_id] = {"Nombre" : nombre,
                                 "Precio" : precio,
                                 "Equipo" : equipo}
                print("Listo, datos ingresados")
                input()
            case 4:
                borrar_id = int(input("Ingresa la ID del jugado que quieres borrar:\n"))
                if borrar_id not in nba:
                    print("Ingresa una id valida")
                else:
                    del nba[borrar_id]
            case 5:
                break

    except Exception as e:
        print("error" ,e)