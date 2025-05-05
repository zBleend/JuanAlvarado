#Calcular el puntaje de credito
#debe calcular que tnanto credito tiene una persona en cierta entidad funcanciera, deberá considerar:
#Cantidad de ingresos, nivel educacional y nacionalidad
#cantidad de ingresos: 500.000/1.000.000 : 300.000
#1.000.000 a 1.500.000: 650.000
#nivel educacional
#basico: x1, medio: x1.3, superior: x1.5
#nacionalidad
#chilena: +300.000, extrajero: +0

ingresofinal=0

ingreso=int(input("""
Bienvenido
Ingrese su credito: (Minimo $500.000, Maximo $1.500.000)
"""))
educacion=int(input("Ingrese su nuvel educacional:\n1.- Basica\n2.- Media\n3.- Superior\n"))
nacionalidad=input("Ingrese su nacionalidad:\n")

if 500000 <= ingreso <= 1000000:
    ingresofinal=ingreso+300000
elif 1000000 <= ingreso <= 1500000:
    ingresofinal=ingreso+650000
elif ingreso > 1500000:
    print("Error: Excede monto")

if educacion==1:
    ingresofinal*=1
elif educacion==2:
    ingresofinal*=1.3
elif educacion==3:
    ingresofinal*=1.5
else:
    print("ERROR: Ingrese un dator valido")

if nacionalidad.upper in ["CHILENA", "CHILENO"]:
    ingresofinal= ingresofinal + 300000
print(f"Su ingreso es de: {ingresofinal}")