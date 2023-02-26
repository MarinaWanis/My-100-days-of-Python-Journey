from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.ball_speed = 0

    def move(self):
        new_xcor = self.xcor() + self.x_direction
        new_ycor = self.ycor() + self.y_direction
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self):
        self.ball_speed += 0.5
        self.speed(self.ball_speed)
