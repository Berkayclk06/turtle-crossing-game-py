import time
from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.game_is_on = True
        self.cars = []
        self.move_speed = 0.1

    def generate_car(self):
        random_num = random.randint(1, 4)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(stretch_wid=2, stretch_len=1)
            new_car.penup()
            new_car.setheading(270)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(250, new_y)
            self.cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - 10
            car.goto(new_x, car.ycor())
            car.speed("slowest")



