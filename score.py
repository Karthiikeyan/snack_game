from turtle import Turtle

FONT = ("Arial",16,"normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0,270)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(arg=f"Score = {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def increase(self):
        self.speed(0)
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}",align="center",font=FONT)

