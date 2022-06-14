from turtle import Screen, Turtle
from ball import Ball
from pod import Pod
#from left_pod import Left_Pod

# Building up table
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

ball = Ball()
right_pod = Pod((350,0))
left_pod = Pod((-350,0))

screen.listen()

screen.onkey(right_pod.move_up, "Up")
screen.onkey(right_pod.move_down, "Down")

screen.onkey(left_pod.move_up, "w")
screen.onkey(left_pod.move_down, "s")


game_is_on=True

while game_is_on:
    screen.update()

screen.exitonclick()
