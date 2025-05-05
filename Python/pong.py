import tkinter as tk

# Configuración inicial
WIDTH = 600
HEIGHT = 400
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
PADDLE_SPEED = 20

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        # Crear la pelota
        self.ball = self.canvas.create_oval(WIDTH//2 - 10, HEIGHT//2 - 10, WIDTH//2 + 10, HEIGHT//2 + 10, fill="white")

        # Crear las paletas
        self.paddle_left = self.canvas.create_rectangle(20, HEIGHT//2 - 40, 30, HEIGHT//2 + 40, fill="white")
        self.paddle_right = self.canvas.create_rectangle(WIDTH - 30, HEIGHT//2 - 40, WIDTH - 20, HEIGHT//2 + 40, fill="white")

        # Velocidad de la pelota
        self.ball_dx = BALL_SPEED_X
        self.ball_dy = BALL_SPEED_Y
        
        # Movimiento de las paletas
        self.root.bind("<w>", lambda event: self.move_paddle(self.paddle_left, -PADDLE_SPEED))
        self.root.bind("<s>", lambda event: self.move_paddle(self.paddle_left, PADDLE_SPEED))
        self.root.bind("<Up>", lambda event: self.move_paddle(self.paddle_right, -PADDLE_SPEED))
        self.root.bind("<Down>", lambda event: self.move_paddle(self.paddle_right, PADDLE_SPEED))

        self.move_ball()

    def move_paddle(self, paddle, dy):
        x1, y1, x2, y2 = self.canvas.coords(paddle)
        if 0 < y1 + dy and y2 + dy < HEIGHT:
            self.canvas.move(paddle, 0, dy)

    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)

        # Rebote en la parte superior e inferior
        if y1 <= 0 or y2 >= HEIGHT:
            self.ball_dy *= -1

        # Rebote en las paletas
        if self.check_collision(self.paddle_left) or self.check_collision(self.paddle_right):
            self.ball_dx *= -1

        # Reiniciar si la pelota sale de los límites
        if x1 <= 0 or x2 >= WIDTH:
            self.canvas.coords(self.ball, WIDTH//2 - 10, HEIGHT//2 - 10, WIDTH//2 + 10, HEIGHT//2 + 10)
            self.ball_dx = BALL_SPEED_X if x1 > 0 else -BALL_SPEED_X

        self.root.after(20, self.move_ball)

    def check_collision(self, paddle):
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(paddle)

        return (paddle_coords[0] < ball_coords[2] and paddle_coords[2] > ball_coords[0] and
                paddle_coords[1] < ball_coords[3] and paddle_coords[3] > ball_coords[1])

root = tk.Tk()
game = PongGame(root)
root.mainloop()