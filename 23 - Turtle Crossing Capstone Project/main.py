import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Se define la pantalla
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Se hace una instanacia de cada clase
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

#Esto es para darle funcionamiento a traves del boton Up.
#Luego de alli se activa ese metodo cada vez que se teclea
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #Se utiliza para saber si el carro y el player se tocaron
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            print(scoreboard.game_over())

    # Back to start position
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        # Increase score
        scoreboard.increase_level()

        
screen.exitonclick()
