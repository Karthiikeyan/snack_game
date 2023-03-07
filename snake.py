from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POSITION = [(0,0),(-20,0),(-40,0)]
# snakes = []

class Snake:

    def __init__(self):
        self.snakes = []
        self.create()
        self.head = self.snakes[0]



    def create(self,):
        for i in POSITION:
            self.add_body(i)


    def add_body(self,i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.speed(10)
        tim.goto(i)
        self.snakes.append(tim)

    def extend(self):
        self.add_body(self.snakes[-1].position())


    def move(self):

        for snake in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[snake - 1].xcor()
            y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)












