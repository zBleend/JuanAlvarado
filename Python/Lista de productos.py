def menu():
    productos = []
    precios = []
    carrito = []
    
    while True:
        try:
            op = int(input("""--- Bienvenido ---
1.- Agregar productos (Nombre producto y precio)
2.- Comprar
3.- Crear Boleta
4.- Salir
"""))
            match op:
                case 1:
                    productos, precios = agregar_productos()
                case 2:
                    ver_productos(productos, precios)
                case 3:
                    generar_boleta(productos, precios)
                case 4:
                    print("--- Adios ---")
                case _:
                    print("Seleccione una opcion valida")
        except Exception:
            print("Seleccione una opcion valida")

def agregar_producto(productos, precios):
    while True:
        nombre = input("Ingrese nombre del producto ('salir' para volver):\n")
        if nombre.lower() == "salir":
            return productos, precios
        else:
            try:
                precio = float(input(f"Ingrese precio de {nombre}:\n"))
                productos.append(nombre)
                precios.append(precio)
            except ValueError:
                print("Ingrese un precio valido")

def ver_productos(productos, precios):
    print("\n--- Lista de productos ---")
    for i in range(len(productos)):
        print(f"{productos[i]} - ${precios[i]:.2f}")
    print("--------------------------")