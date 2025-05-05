import tkinter as tk
import random

# Configuración inicial
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
MOVE_SPEED = 100

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.root.resizable(False, False)

        # Crear la interfaz
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.label_score = tk.Label(self.frame, text="Puntos: 0", font=("Arial", 14))
        self.label_score.pack()

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Inicializar serpiente y comida
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.food = self.place_food()
        self.direction = "Right"
        self.running = True
        self.score = 0

        # Controles
        self.root.bind("<Up>", lambda event: self.change_direction("Up"))
        self.root.bind("<Down>", lambda event: self.change_direction("Down"))
        self.root.bind("<Left>", lambda event: self.change_direction("Left"))
        self.root.bind("<Right>", lambda event: self.change_direction("Right"))

        self.root.bind("<w>", lambda event: self.change_direction("Up"))
        self.root.bind("<s>", lambda event: self.change_direction("Down"))
        self.root.bind("<a>", lambda event: self.change_direction("Left"))
        self.root.bind("<d>", lambda event: self.change_direction("Right"))

        self.update()

    def place_food(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)

    def change_direction(self, new_direction):
        opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move_snake(self):
        if not self.running:
            return

        x, y = self.snake[-1]
        if self.direction == "Up":
            y -= CELL_SIZE
        elif self.direction == "Down":
            y += CELL_SIZE
        elif self.direction == "Left":
            x -= CELL_SIZE
        elif self.direction == "Right":
            x += CELL_SIZE

        new_head = (x, y)

        # Colisión con bordes o cuerpo
        if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT or new_head in self.snake:
            self.game_over()
            return

        self.snake.append(new_head)

        # Comer comida
        if new_head == self.food:
            self.food = self.place_food()
            self.score += 1
            self.label_score.config(text=f"Puntos: {self.score}")
        else:
            self.snake.pop(0)

    def update(self):
        self.move_snake()
        self.canvas.delete("all")

        # Dibujar comida
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + CELL_SIZE, self.food[1] + CELL_SIZE, fill="red")

        # Dibujar serpiente
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="green")

        if self.running:
            self.root.after(MOVE_SPEED, self.update)

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="red", font=("Arial", 24))
        
        # Agregar botones de reiniciar y salir
        self.button_restart = tk.Button(self.frame, text="Jugar de nuevo", command=self.restart, font=("Arial", 12))
        self.button_restart.pack()
        self.button_exit = tk.Button(self.frame, text="Salir", command=self.root.quit, font=("Arial", 12))
        self.button_exit.pack()

    def restart(self):
        self.snake = [(WIDTH // 2, HEIGHT // 2)]
        self.food = self.place_food()
        self.direction = "Right"
        self.running = True
        self.score = 0
        self.label_score.config(text="Puntos: 0")

        self.button_restart.destroy()
        self.button_exit.destroy()

        self.update()

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()