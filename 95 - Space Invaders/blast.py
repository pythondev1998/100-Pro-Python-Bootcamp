from turtle import Turtle

class Blast(Turtle):
    def __init__(self, level):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.shapesize(stretch_wid=0.1, stretch_len=1)
        self.up()
        self.y_move = 15  # Ajusta este valor para controlar la velocidad de disparo
        
        # Ajusta la velocidad de movimiento del proyectil según el nivel
        if level == 1:
            self.move_speed = 0.02
        elif level == 2:
            self.move_speed = 0.03
        elif level == 3:
            self.move_speed = 0.04

    def move(self):
        self.forward(self.y_move)
