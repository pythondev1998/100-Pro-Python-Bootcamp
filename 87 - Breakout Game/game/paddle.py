# game/paddle.py

import turtle

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        x = self.xcor()
        x -= 30  # Aumenta la cantidad de píxeles para el movimiento hacia la izquierda
        if x < -290:
            x = -290
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += 30  # Aumenta la cantidad de píxeles para el movimiento hacia la derecha
        if x > 290:
            x = 290
        self.setx(x)

# Comentario:
# La clase Paddle representa la pala del jugador y define su apariencia y comportamiento.
# Tiene métodos para mover la pala hacia la izquierda y la derecha.
