from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars():
    def __init__(self):
        self.car_list = []
        # self.x_cor = 0
        self.car_position = []
        self.new_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        i = random.randint(1, 6)
        if i == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(400, random.randint(-230, 230))
            car.shape("square")
            car.shapesize(stretch_len=2)
            self.car_list.append(car)

    def move_cars(self):
        for each_car in self.car_list:
            each_car.backward(self.new_speed)
            # self.x_cor = each_car.xcor()
            # self.y_cor = each_car.ycor()
            self.car_position.append(each_car.position())
            # self.car_position = each_car.position()

    def reset_car_positions(self):
        self.car_position.clear()

    def speed_up_cars(self):
        self.new_speed += MOVE_INCREMENT
        for each_car in self.car_list:
            each_car.backward(self.new_speed)


