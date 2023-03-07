from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("skyblue")
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.penup()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)