from turtle import Screen, Turtle
from ball import Ball
from pod import Pod
import time

# Building up table
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

ball = Ball()
right_pod = Pod((350, 0))
left_pod = Pod((-350, 0))

screen.listen()

screen.onkey(right_pod.move_up, "Up")
screen.onkey(right_pod.move_down, "Down")

screen.onkey(left_pod.move_up, "w")
screen.onkey(left_pod.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if ball.xcor() == 0 and ball.ycor() == 0:
        ball.norteast()
        ball.move()

    elif ball.ycor() > 290:  # or ball.ycor() < -290:
        ball.soutwest()
        ball.move()

    elif ball.xcor() > 350:  # or ball.ycor() < -350:
        ball.souteast()
        ball.move()

    elif ball.ycor() < -290:  # or ball.ycor() < -350:
        ball.nortwest()
        ball.move()

    elif ball.xcor() < -350:  # or ball.ycor() < -290:
        ball.norteast()
        ball.move()

    else:
        ball.move()

screen.exitonclick()
