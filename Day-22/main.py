from turtle import Screen, Turtle
from ball import Ball
from pod import Pod

# Building up table
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")

ball = Ball()
pod = Pod()

screen.listen()
screen.onkey(pod.move_up, "Up")
screen.onkey(pod.move_down, "Down")

screen.exitonclick()
