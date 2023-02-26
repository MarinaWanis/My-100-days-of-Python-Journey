from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)


def set_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r,g,b)
    return color_tuple


timmy.speed(0)
angle = 1


def draw_spirograph(current_angle):
    for _ in range(int(360/angle)):
        timmy.color(set_color())
        timmy.circle(100)
        current_angle += angle
        timmy.setheading(current_angle)


draw_spirograph(angle)
screen.exitonclick()

