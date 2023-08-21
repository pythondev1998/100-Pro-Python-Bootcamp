from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../data.txt") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # TODO Create a scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"You score is {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
