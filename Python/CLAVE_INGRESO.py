print("*************************************")
print("--------Bienvenido al sistema--------")
print("*************************************")

def inicio_de_sesion():
    clave="mamahuevo"
    clave=input("Ingrese su clave: ")

    while clave!="mamahuevo":
        print("Clave incorrecta")
        clave=input("Ingrese su clave: ")

    if clave=="mamahuevo":
        print("Bienvenido al sistema")

inicio_de_sesion()