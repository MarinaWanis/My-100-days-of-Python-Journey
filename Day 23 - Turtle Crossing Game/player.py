from turtle import Turtle
MOVE_DISTANCE =10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5)
        self.setheading(90)
        self.penup()
        self.goto(0,-300)

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(0,-300)

