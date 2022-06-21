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
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.restart()
        scoreboard.level_up()

    # Detect car collision
    for car in car_manager.cars:  # Looping throught the list cars
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
