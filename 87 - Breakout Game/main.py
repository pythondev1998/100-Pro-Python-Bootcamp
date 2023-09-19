import turtle
from game.screen import Screen
from game.paddle import Paddle
from game.ball import Ball
from game.bricks import Bricks
from utils.collision_handler import CollisionHandler
from utils.scoreboard import Scoreboard

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 600
screen = Screen(WIDTH, HEIGHT)

# Crear los elementos del juego
paddle = Paddle()
ball = Ball()
bricks = Bricks()
collision_handler = CollisionHandler()
scoreboard = Scoreboard()

# Manejo de eventos de teclado para el movimiento de la pala
screen.window.listen()
screen.window.onkeypress(paddle.move_left, "Left")
screen.window.onkeypress(paddle.move_right, "Right")

# Loop principal del juego
game_over = False
while not game_over:
    ball.move(paddle)  # Pasa la instancia 'paddle' como argumento al método 'move()' de la clase 'Ball'

    # Verificar colisiones con la pala
    if collision_handler.check_collision(ball, paddle):
        ball.bounce_y()

    # Verificar colisiones con los ladrillos
    for brick in bricks.get_bricks():
        if collision_handler.check_collision(ball, brick):
            ball.bounce_y()
            bricks.remove(brick)
            scoreboard.increase_score()

    # Verificar si el jugador ha ganado o perdido
    if len(bricks.get_bricks()) == 0:
        scoreboard.you_win()
        game_over = True

    if ball.ycor() < -290:
        scoreboard.game_over()
        game_over = True

    screen.update()

# Cerrar la pantalla al hacer clic
screen.window.exitonclick()
