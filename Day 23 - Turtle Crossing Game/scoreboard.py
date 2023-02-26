from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-360, 260)
        self.hideturtle()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center", font=FONT)


