import turtle
from turtle import Turtle,Screen
import random
# import colorgram

timmy = Turtle()
screen = Screen()

# colors = colorgram.extract('Hirst Painting.jpg', 30)
# color_list = []
# for color in colors:
#     # first_color = colors
#     rgb = color.rgb
#     color_tuple = (rgb.r, rgb.g, rgb.b)
#     color_list.append(color_tuple)

color_list = [(201, 157, 111), (63, 104, 125), (153, 84, 51), (124, 81, 96), (126, 162, 175), (133, 173, 160)]

timmy.speed(1)
turtle.colormode(255)
move_up= -180.31

timmy.penup()
timmy.setheading(225)
timmy.forward(255)
timmy.setheading(0)

print(timmy.position())

for _ in range(10):
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
    move_up += 50
    timmy.setposition(-180.31, move_up)

screen.exitonclick()
