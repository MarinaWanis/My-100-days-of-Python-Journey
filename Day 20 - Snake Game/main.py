from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.segments[0].distance(food) < 20:
        food.refresh()
        scoreboard.add_score()
        snake.add_segment()

    # snake collides with walls
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -290:
        scoreboard.update_highest_score()
        snake.clear_snake()

    # snake collides with body
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg) < 1:
            scoreboard.update_highest_score()
            snake.clear_snake()


screen.exitonclick()
