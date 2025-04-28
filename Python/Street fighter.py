import random
import time
import os

def limpiar_pantalla():
    os.system('cls')

def inicio_jugadores():
    print("""
***************************
Bienvenido a Street Fighter
***************************
          """)
    time.sleep(1)
    jugador1=input("Ingresa a tu jugador 1\n")
    jugador2=input("Ingresa a tu jugador 2\n")
    return jugador1, jugador2

def turnos(jugador1, jugador2):
    hp1=50
    hp2=50
    limpiar_pantalla()
    print(f"Los peleadores son: {jugador1} y {jugador2}")
    time.sleep(1)
    return jugador1, jugador2, hp1, hp2

def sistema(jugador1, jugador2, hp1, hp2):
    turno=random.randint(1,2)
    while hp1>0 and hp2>0:
        if turno %2==0:
            print(f"Turno de {jugador1}")
            atk=random.randint(3,15)
            critical=random.randint(1,5)
            if critical==3:
                print(f"¡HUBO DAÑO CRITICO DE {jugador1}!")
                atk*=2
            hp2-=atk
            print(f"Vida de {jugador2}")
            print("/"*hp2)
            turno+=1
        else:
            print(f"Turno de {jugador2}")
            atk=random.randint(3,15)
            critical=random.randint(1,5)
            if critical==3:
                print(f"¡HUBO DAÑO CRITICO DE {jugador2}!")
                atk*=2
            hp1-=atk
            print(f"Vida de {jugador1}")
            print("/"*hp1)
            turno+=1
        time.sleep(1)
        limpiar_pantalla()
    print("¡TENEMOS UN GANADOR!")
    time.sleep(1)

def ganador(jugador1, jugador2, hp1, hp2):
    limpiar_pantalla()
    print("El ganador es...")
    time.sleep(1)
    if hp2 <= 0 and hp1 <= 0:
        print(f"¡ES UN EMPATE!")
    elif hp1 <=0:
        print(f"El ganador es {jugador1}")
    else:
        print(f"El ganador es {jugador2}")

if __name__ == "__main__":
    jugador1, jugador2 = inicio_jugadores()
    jugador1, jugador2, hp1, hp2 = turnos(jugador1, jugador2)
    sistema(jugador1, jugador2, hp1, hp2)
    ganador(jugador1, jugador2, hp1, hp2)