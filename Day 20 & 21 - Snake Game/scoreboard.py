from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.read_highest_score()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        # self.read_highest_score()

    def update_scoreboard(self):
        self.clear()
        self.read_highest_score()
        self.write(f"Score: {self.score} Highest_Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def read_highest_score(self):
        with open("../../Desktop/highest score.txt", mode="r") as file:
            return int(file.read())

    def update_highest_score(self):
        if self.score > self.highest_score:
            with open("../../Desktop/highest score.txt", mode="w") as file:
                file.write(str(self.score))
        self.highest_score = self.read_highest_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
