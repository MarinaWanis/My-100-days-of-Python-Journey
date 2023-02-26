from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()

game_is_on = True
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball= Ball()

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

xcor = 0
ycor = 0
speed = 0.1

while game_is_on:
    print(speed)
    time.sleep(speed)
    screen.update()
    ball.move()

    # ball collides with the up and down walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # ball collides with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 330 or ball.distance(l_paddle) < 50 and ball.xcor() <= -330:
        ball.bounce_x()
        speed *= 0.9


    # right paddles miss the ball
    if ball.xcor() > 390:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.add_l_paddle_score()
        speed = 0.1

    # left paddle misses the ball
    if ball.xcor() < -390:
        time.sleep(0.5)
        ball.reset_position()
        scoreboard.add_r_paddle_score()


screen.exitonclick()
