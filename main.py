import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect finish line
    if player.ycor() == player.FINISH_LINE_Y:
        player.goto(player.STARTING_POSITION)
        scoreboard.level_up()
        car_manager.move_speed *= 0.9

    # Detect collision with cars
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False

    time.sleep(car_manager.move_speed)
    screen.update()

scoreboard.game_over()
screen.exitonclick()
