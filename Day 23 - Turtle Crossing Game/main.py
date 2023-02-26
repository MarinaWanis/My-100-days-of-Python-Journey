from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
scoreboard = Scoreboard()
game_is_on = True

timmy = Player()


screen.listen()
screen.onkeypress(timmy.move_turtle, "Up")

car = Cars()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    # Detect collision with a car
    for each_car_position in car.car_position:
        # print(timmy.distance(each_car_position))
        if timmy.distance(each_car_position) < 30:
            # print(timmy.distance(each_car_position))
            # timmy.reset_turtle()
            scoreboard.game_over()
            game_is_on = False

    car.reset_car_positions()

    #turtle reaches the finish line
    if timmy.ycor() >= 280:
        timmy.reset_turtle()
        car.speed_up_cars()
        scoreboard.level_up()
        # print(car.new_speed)


screen.exitonclick()
