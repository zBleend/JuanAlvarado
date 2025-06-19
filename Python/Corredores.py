corredores = ["Slatan", "Bombasi", "Lando"]
tiempos = [10.9, 11.1, 12.5]
while True:
    try:
        op = int(input("""1.- Registrar Corredor y tiempo
2.- Ver listado de corredores
3.- Ver estadisticas
4.- Salir
"""))
        match op:
            case 1:
                corre = input("\nIngrese el nombre del corredor:\n")
                corredores.append(corre)
                tie = float(input("Registre su mejor tiempo:\n"))
                tiempos.append(tie)
            case 2:
                for n in range (len(corredores)):
                    print(corredores[n], tiempos[n])
            case 3:
                print()
            case 4:
                break
            case _:
                print("Elija una opcion valida")
    except ValueError:
        print("Error Seleccione una opcion valida")