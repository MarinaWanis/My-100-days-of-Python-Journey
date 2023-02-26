import time
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, -0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """Creating the body of the snake with 3 segments"""
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.create_segment(pos)

    def create_segment(self, position):
        create_segment = Turtle()
        create_segment.shape("square")
        create_segment.penup()
        create_segment.color("white")
        create_segment.goto(position)
        self.segments.append(create_segment)

    def add_segment(self):
       self.create_segment(self.segments[-1].position())

    def move_snake(self):
        # for seg_index in range (start=,stop=,step=)
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_index - 1].xcor()
            new_ycor = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_xcor, new_ycor)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def clear_snake(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.move_snake()
        time.sleep(0.5)


