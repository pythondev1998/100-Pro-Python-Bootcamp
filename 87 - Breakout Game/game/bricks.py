import turtle

class Bricks:
    def __init__(self):
        self.bricks = []
        colors = ["red", "orange", "yellow", "green", "blue"]
        for y in range(5):
            color = colors[y]
            for x in range(-280, 300, 60):
                brick = turtle.Turtle()
                brick.shape("square")
                brick.color(color)
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.penup()
                brick.goto(x, 250 - y * 30)
                self.bricks.append(brick)

    def remove(self, brick):
        brick.hideturtle()
        self.bricks.remove(brick)

    def get_bricks(self):
        return self.bricks

# Comentario:
# La clase Bricks representa la estructura de ladrillos que el jugador debe destruir.
# Se crea una disposición de ladrillos de colores y tiene métodos para eliminar ladrillos.
