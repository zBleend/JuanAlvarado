def clave():
    texto = input("Ingrese su contraseña:\n")
    return texto

def validar_clave():
    while True:
        texto = clave()
        if len(texto) < 6:
            print("La clave tiene que tener un minimo de 6 caracteres")
        elif not any(c.isdigit() for c in texto):
            print("La clave debe de tener al menos un numero")
        elif sum(1 for c in texto if c.isupper()) < 3:
            print("La clave debe de tener al menos 3 letras mayúsculas")
        elif not any(c.islower() for c in texto):
            print("La clave debe de tener una minuscula")
        elif sum(1 for c in texto if c.isdigit()) < 3:
            print("La clave debe de tener 3 numeros como minimo")
        elif "#" not in texto:
            print('La clave debe de incluir un "#" ')
        else:
            return True

def bienvenida():
    if validar_clave() == True:
        print("Clave exitosa Bienvenido")

bienvenida()