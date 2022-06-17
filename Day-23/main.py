from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Turtle Crossing Game")
screen.tracer(0)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
