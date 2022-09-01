from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.MOVE_DISTANCE = 10
        self.FINISH_LINE_Y = 280
        self.STARTING_POSITION = (0, -280)
        self.goto(self.STARTING_POSITION)

    def move(self):
        self.forward(self.MOVE_DISTANCE)
