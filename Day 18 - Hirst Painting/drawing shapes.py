from turtle import Turtle, Screen
# import random
timmy = Turtle()
screen = Screen()

sides = 3
degrees = 360
shapes = 1

color_list = ["green", "red", "black", "grey", "blue", "pink", "brown", "purple", "orange", "brown"]

while shapes <= 10:
    shape_angle = degrees / sides
    # random_color = random.choice(color_list)
    timmy.pencolor(color_list[shapes-1])
    for i in range(sides):
        timmy.forward(100)
        timmy.right(shape_angle)
    sides += 1
    shapes += 1



screen.exitonclick()
