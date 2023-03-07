from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
# screen.tracer(0)


mini = Snake()
score = Score()
food = Food()

screen.onkey(mini.up, "Up")
screen.onkey(mini.down, "Down")
screen.onkey(mini.left, "Left")
screen.onkey(mini.right, "Right")

screen.listen()

on_game = True

while on_game:


    mini.move()
    if mini.head.distance(food) < 15:
        # screen.update()
        food.refresh()
        mini.extend()
        score.increase()

    if mini.head.xcor() > 280 or mini.head.xcor() < -280 or mini.head.ycor() > 280 or mini.head.ycor() < -280:
        score.game_over()
        on_game = False

    for snake in mini.snakes[1:]:

        if mini.head.distance(snake) < 10:
            on_game = False
            score.game_over()


screen.exitonclick()