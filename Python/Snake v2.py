import random
import time
import os
import sys
try:
    import msvcrt  # Para Windows
except ImportError:
    pass  # Para otros sistemas operativos

# Configuración del juego
ANCHO = 20
ALTO = 10
SERPIENTE = '*'
COMIDA = '♥'
VACIO = '□'
DIRECCIONES = {'w': 'arriba', 's': 'abajo', 'a': 'izquierda', 'd': 'derecha'}

class SnakeGame:
    def __init__(self):
        self.ancho = ANCHO
        self.alto = ALTO
        self.serpiente = [[self.alto//2, self.ancho//2]]
        self.direccion = 'derecha'
        self.comida = self.generar_comida()
        self.puntos = 0
        self.game_over = False
        
    def generar_comida(self):
        while True:
            comida = [random.randint(0, self.alto-1), random.randint(0, self.ancho-1)]
            if comida not in self.serpiente:
                return comida
    
    def dibujar_tablero(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
        
        # Dibujar bordes y contenido
        print("+" + "-" * self.ancho + "+")
        for y in range(self.alto):
            fila = "|"
            for x in range(self.ancho):
                if [y, x] == self.comida:
                    fila += COMIDA
                elif [y, x] in self.serpiente:
                    fila += SERPIENTE
                else:
                    fila += VACIO
            fila += "|"
            print(fila)
        print("+" + "-" * self.ancho + "+")
        print(f"Puntos: {self.puntos} | Controles: WASD | Salir: Q")
    
    def mover(self):
        cabeza = self.serpiente[0].copy()
        
        # Mover cabeza según dirección
        if self.direccion == 'arriba':
            cabeza[0] -= 1
        elif self.direccion == 'abajo':
            cabeza[0] += 1
        elif self.direccion == 'izquierda':
            cabeza[1] -= 1
        elif self.direccion == 'derecha':
            cabeza[1] += 1
        
        # Verificar colisiones
        if (cabeza[0] < 0 or cabeza[0] >= self.alto or
            cabeza[1] < 0 or cabeza[1] >= self.ancho or
            cabeza in self.serpiente):
            self.game_over = True
            return
        
        # Insertar nueva cabeza
        self.serpiente.insert(0, cabeza)
        
        # Verificar si comió
        if cabeza == self.comida:
            self.puntos += 1
            self.comida = self.generar_comida()
        else:
            # Quitar cola si no comió
            self.serpiente.pop()
    
    def cambiar_direccion(self, tecla):
        tecla = tecla.lower()
        if tecla in DIRECCIONES:
            nueva_dir = DIRECCIONES[tecla]
            # Evitar movimiento opuesto al actual
            if not ((self.direccion == 'arriba' and nueva_dir == 'abajo') or
                   (self.direccion == 'abajo' and nueva_dir == 'arriba') or
                   (self.direccion == 'izquierda' and nueva_dir == 'derecha') or
                   (self.direccion == 'derecha' and nueva_dir == 'izquierda')):
                self.direccion = nueva_dir

def get_key():
    """Obtiene una tecla presionada, compatible con Windows y otros sistemas"""
    if os.name == 'nt':  # Windows
        try:
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8')
        except:
            return None
    else:  # Linux/Mac
        try:
            import tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        except:
            return None
    return None

def mostrar_mensaje_final(puntos):
    print("\n¡Game Over!")
    print(f"Puntuación final: {puntos}")
    print("\n¿Quieres jugar de nuevo? (S/N)")
    
    while True:
        tecla = get_key()
        if tecla:
            if tecla.lower() == 's':
                return True
            elif tecla.lower() == 'n':
                return False

def jugar_partida():
    juego = SnakeGame()
    
    print("Snake Game - Controles: WASD para mover, Q para salir")
    print("Presiona cualquier tecla para comenzar...")
    get_key()  # Espera a que el usuario presione una tecla
    
    try:
        while not juego.game_over:
            juego.dibujar_tablero()
            
            # Obtener entrada del usuario
            tecla = get_key()
            if tecla:
                if tecla.lower() == 'q':
                    break
                juego.cambiar_direccion(tecla)
            
            juego.mover()
            time.sleep(0.2)
        
        juego.dibujar_tablero()
        return juego.puntos
    
    except KeyboardInterrupt:
        print("\nJuego terminado por el usuario")
        return 0

def main():
    jugar_de_nuevo = True
    
    while jugar_de_nuevo:
        puntos = jugar_partida()
        jugar_de_nuevo = mostrar_mensaje_final(puntos)
        if jugar_de_nuevo:
            os.system('cls' if os.name == 'nt' else 'clear')

    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main()