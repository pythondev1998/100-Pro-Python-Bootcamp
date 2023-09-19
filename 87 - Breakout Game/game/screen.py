import turtle

class Screen:
    def __init__(self, width, height):
        self.window = turtle.Screen()
        self.window.title("Breakout")
        self.window.setup(width, height)
        self.window.bgcolor("black")
        self.window.tracer(0)

    def update(self):
        self.window.update()

    def close(self):
        self.window.bye()

# Comentario:
# La clase Screen se encarga de crear la pantalla del juego y controlar su aspecto.
# Proporciona métodos para actualizar la pantalla y cerrarla.
