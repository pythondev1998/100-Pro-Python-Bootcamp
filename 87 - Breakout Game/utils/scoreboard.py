import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 10
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 30, "normal"))

    def you_win(self):
        self.goto(0, 0)
        self.write("You Win!", align="center", font=("Courier", 30, "normal"))

# Comentario:
# La clase Scoreboard se encarga de mostrar la puntuación en la pantalla
# y mensajes relevantes como "Game Over" o "You Win".
