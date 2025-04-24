import random
import os
op=None
numAl= random.randint (1,20)
print("Bienvenido al juego del adivinador\nIngresa un numero a ver si adivinas cual es, tienes 5 intentos\n¡Mucha suerte!")
intento=5
while intento==0 or op!=numAl:
    op=int(input("Ingresa tu numero:\n"))
    if op<numAl:
        print(f"El numero es mayor, intenta de nuevo, tienes {intento-1} intentos")
        intento-=1
    elif op==numAl:
        break
    else:
        print(f"El numero es menor, intenta de nuevo, tienes {intento-1} intentos")
        intento-=1
if intento==-1 or op==numAl:
    os.system('cls')
if op==numAl:
    print(f"Felicidades, el numero era: {numAl}")
else:
    print(f"Lo lamento, haz fallado, el numero era: {numAl}, mas suerte para la proxima")