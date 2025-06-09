def menu():
    productos = []
    precios = []
    
    while True:
        try:
            op = int(input("""--- Bienvenido ---
1.- Agregar producto
2.- Ver productos
3.- Generar boleta
4.- Salir
"""))
            match op:
                case 1:
                    productos, precios = agregar_producto(productos, precios)
                case 2:
                    ver_productos(productos, precios)
                case 3:
                    generar_boleta(productos, precios)
                case 4:
                    print("--- Adios ---")
                    break
                case _:
                    print("Seleccione una opcion válida")    
        except Exception:
            print("Seleccione una opción válida")


def agregar_producto(productos, precios):
    while True:
        nombre = input("Ingrese nombre del producto ('salir' para volver):\n")
        if nombre.lower() == "salir":
            return productos, precios
        else:
            try:
                precio = float(input(f"Ingrese precio de {nombre}: "))
                productos.append(nombre)
                precios.append(precio)
            except ValueError:
                print("Ingrese un precio válido")


def ver_productos(productos, precios):
    print("\n--- Lista de productos ---")
    for i in range(len(productos)):
        print(f"{productos[i]} - ${precios[i]:.2f}")
    print("--------------------------")


def generar_boleta(productos, precios):
    print("\n--- Boleta ---")
    total = 0
    for i in range(len(productos)):
        print(f"{productos[i]} - ${precios[i]:.2f}")
        total += precios[i]
    print("--------------------------")
    print(f"Total a pagar: ${total:.2f}")
    print("--------------------------")


menu()