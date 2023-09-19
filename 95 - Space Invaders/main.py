from turtle import Screen, Turtle, numinput
import time
from ship import Ship
from blast import Blast
from invaders import Invaders

def strike():
    if not blast.isvisible():
        blast.setheading(90)
        blast.goto(x=ship.xcor(), y=-250)
        blast.showturtle()

def change_level(level):
    global invader_speed, num_rows, num_invaders_per_row
    if level == 1:
        invader_speed = 6
        num_rows = 3
        num_invaders_per_row = 5
    elif level == 2:
        invader_speed = 7
        num_rows = 3
        num_invaders_per_row = 5
    elif level == 3:
        invader_speed = 8
        num_rows = 3
        num_invaders_per_row = 5
    return invader_speed, num_rows, num_invaders_per_row

screen = Screen()
screen.setup(width=800, height=600)
screen.register_shape('img/alien.gif')
screen.register_shape('img/ship.gif')
screen.register_shape('img/new-back.gif')
screen.bgpic("img/back.gif")

screen.title("SpaceInvaders")
screen.tracer(0)

level = 1  # Comenzar siempre desde el nivel 1

ship = Ship()
invader_speed, num_rows, num_invaders_per_row = change_level(level)
aliens = Invaders(num_rows=num_rows, num_invaders_per_row=num_invaders_per_row)
blast = Blast(level=level)
blast.hideturtle()

screen.listen()
screen.onkeypress(fun=ship.move_left, key="Left")
screen.onkeypress(fun=ship.move_right, key="Right")
screen.onkeypress(fun=strike, key="Up")

game_is_on = True
score = 0

score_display = Turtle()
score_display.color("white")
score_display.up()
score_display.hideturtle()
score_display.goto(-350, 250)
score_display.write(f"Score: {score}", align="left", font=('Distant Galaxy', 18, 'normal'))

while game_is_on:
    time.sleep(0.025)
    screen.update()
    blast.move()

    for m in aliens.all_invaders:
        m.forward(invader_speed)

    if blast.ycor() > 280:
        blast.hideturtle()

    for j in aliens.all_invaders:
        if j.xcor() > 360 or j.xcor() < -360:
            y = j.ycor()
            y -= 80
            j.right(180)
            j.sety(y)

        if j.distance(blast) < 40:
            j.hideturtle()
            j.goto(-1000, 1000)
            score += 10  # Sumar 10 puntos por cada enemigo eliminado.
            blast.hideturtle()
            blast.goto(-1000, 1000)
            score_display.clear()  # Borrar el puntaje anterior
            score_display.write(f"Score: {score}", align="left", font=('Distant Galaxy', 18, 'normal'))  # Mostrar el puntaje actualizado

        if j.distance(ship) < 45:
            you_lose = Turtle()
            you_lose.color("red")
            you_lose.up()
            you_lose.hideturtle()
            you_lose.goto(0, 0)
            you_lose.write(arg="Game is over!", align="center", font=('Distant Galaxy', 24, 'normal'))
            game_is_on = False
            time.sleep(1)
            print("Game is over start app again!")
            exit()

    if score >= 150 and level == 1:
        level = 2
        invader_speed, num_rows, num_invaders_per_row = change_level(level)
        ship.goto(0, -250)
        aliens = Invaders(num_rows=num_rows, num_invaders_per_row=num_invaders_per_row)
        blast = Blast(level=level)
        blast.hideturtle()
        screen.update()

    elif score >= 300 and level == 2:
        level = 3
        invader_speed, num_rows, num_invaders_per_row = change_level(level)
        ship.goto(0, -250)
        aliens = Invaders(num_rows=num_rows, num_invaders_per_row=num_invaders_per_row)
        blast = Blast(level=level)
        blast.hideturtle()
        screen.update()

    elif score >= 450:
        you_win = Turtle()
        you_win.color("green")
        you_win.up()
        you_win.hideturtle()
        you_win.goto(0, 0)
        you_win.write(arg="You won!!!", align="center", font=('Distant Galaxy', 24, 'normal'))
        game_is_on = False
screen.exitonclick()
