from turtle import Screen, Turtle
import time
import turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 280:
        player.restart()
        scoreboard.level_up()

screen.exitonclick()
