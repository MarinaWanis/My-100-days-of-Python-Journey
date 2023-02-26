from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(170, 220)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        self.goto(-170, 220)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))

    def add_r_paddle_score(self):
        self.r_score += 1
        self.show_score()

    def add_l_paddle_score(self):
        self.l_score += 1
        self.show_score()
