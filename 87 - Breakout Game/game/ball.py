# game/ball.py

import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2
        self.dy = 2

    def move(self, paddle):  # Agrega 'paddle' como parámetro
        # Actualizar la posición de la pelota en cada iteración
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

        # Verificar colisiones con los extremos laterales
        if self.xcor() > 290 or self.xcor() < -290:
            self.bounce_x()

        # Verificar colisiones con la parte superior de la pala
        if (self.ycor() < -240) and (self.xcor() > paddle.xcor() - 60) and (self.xcor() < paddle.xcor() + 60):
            self.bounce_y()

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1
