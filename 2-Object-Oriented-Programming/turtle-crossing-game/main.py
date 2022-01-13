import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

# Initiates game components
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Initiates screen and connects keys to methods
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, 'Up')

# Plays game and calls methods when needed
on = True
while on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.car_list:
        if car.distance(player) < 20:
            on = False
    if player.at_finish_line():
        player.reset_player()
        scoreboard.score_update()
        cars.speed_up()

scoreboard.gameover()
screen.exitonclick()