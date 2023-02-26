import turtle as t
from turtle import Screen
import random
color_list = ["red", "green", "blue", "purple", "orange"]
turtle_list = []

game_is_on = False
screen = Screen()
screen.setup(width=700, height=500)
gap = 0


user_turtle = t.textinput(title="Make your bet on which turtle will win:", prompt="Choose on of the rainbow color turtles")

while user_turtle not in color_list:
    user_turtle = t.textinput(title="Make your bet on which turtle will win:",
                              prompt=f"Choose one of the colors {color_list}")


for i in range(0, 5):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    gap += 60
    turtle_list.append(new_turtle)
    new_turtle.setposition(x=-330, y=-190 + gap)

if user_turtle:
    game_is_on = True

while game_is_on:

    for turtle in turtle_list:
        if turtle.xcor() > 330:
            game_is_on = False
            if user_turtle == turtle.pencolor():
                print(f'You won! The {turtle.pencolor()} turtle has won the race.')
            else:
                print(f"You lost, the winner of the race is the {turtle.pencolor()} turtle")
        random_speed = random.randint(1, 10)
        turtle.forward(random_speed)

screen.exitonclick()
