import turtle as t
from turtle import Screen
import random

timmy = t.Turtle()
screen = Screen()
# color_list = ["green", "red", "black", "grey", "blue", "pink", "brown", "purple", "orange", "brown"]
direction = [0, 90, 180, 270, 360]


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


t.colormode(255)
# screen.screensize(1000,1000)

random_direction = random.choice(direction)

timmy.speed(0)
timmy.pensize(10)

for _ in range(10000):
    timmy.color(set_color())
    random_direction = random.choice(direction)
    timmy.forward(20)
    timmy.left(random_direction)


screen.exitonclick()
