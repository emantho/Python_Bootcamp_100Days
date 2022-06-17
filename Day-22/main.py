from turtle import Screen, Turtle
from ball import Ball
from pod import Pod
import time
from scoreboard import Scoreboard

# Building up table
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

ball = Ball()
right_pod = Pod((350, 0))
left_pod = Pod((-350, 0))
scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_pod.move_up, "Up")
screen.onkey(right_pod.move_down, "Down")

screen.onkey(left_pod.move_up, "w")
screen.onkey(left_pod.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #game_is_on = False
        ball.bounce_y()

    # Detect collision with Pods
    if ball.distance(right_pod) < 70 and ball.xcor() > 320 or ball.distance(left_pod) < 70 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right pod misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.speed()

    # detect when left pod misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
