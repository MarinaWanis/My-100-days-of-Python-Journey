from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(paddle_position)

    def move_up(self):
        new_ycor = self.ycor() + 20
        xcor = self.xcor()
        self.goto(x=xcor, y=new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        xcor = self.xcor()
        self.goto(x=xcor, y=new_ycor)
