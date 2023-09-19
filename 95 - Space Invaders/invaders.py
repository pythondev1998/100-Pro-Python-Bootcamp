from turtle import Turtle

class Invaders:
    def __init__(self, num_rows, num_invaders_per_row):
        self.all_invaders = []
        x_pos = self.calculate_x_positions(num_invaders_per_row)
        y_pos = self.calculate_y_positions(num_rows)
        for i in range(num_rows):
            for m in range(num_invaders_per_row):
                self.invader = Turtle()
                self.invader.color("grey")
                self.invader.shape("img/alien.gif")
                self.invader.up()
                self.invader.setheading(0)
                self.invader.shapesize(stretch_wid=1, stretch_len=2, outline=0)
                self.invader.goto(x_pos[m], y_pos[i])
                self.all_invaders.append(self.invader)

    def calculate_x_positions(self, num_invaders_per_row):
        x_pos = []
        start_x = -350
        space_between_invaders = 70
        for i in range(num_invaders_per_row):
            x_pos.append(start_x + i * space_between_invaders)
        return x_pos

    def calculate_y_positions(self, num_rows):
        y_pos = []
        start_y = 270
        space_between_rows = 30
        for i in range(num_rows):
            y_pos.append(start_y - i * space_between_rows)
        return y_pos

