from turtle import Turtle, Screen
import random
import turtle

eder = Turtle()
eder.shape("turtle")

colors = [Rgb(r=242, g=243, b=245), Rgb(r=230, g=228, b=224), Rgb(
    r=236, g=241, b=238), Rgb(r=241, g=236, b=240), Rgb(r=198, g=159, b=116)]
# colors = [
#     "dark gray",
#     "black",
#     "deep sky blue",
#     "lime green",
#     "firebrick",
#     "red",
#     "purple",
#     "yellow",
# ]

# TODO: Create a random walk for the turtle
direction = [0, 90, 180, 270]
size = 10

for _ in range(100):
    eder.setheading(random.choice(direction))
    eder.forward(30)

# TODO: Use random color when turtle moves
    eder.pen(pencolor=random.choice(colors), pensize=size)

# TODO: Increment the ticker of the line 👆

# TODO: Speed up the turtle when moving
    eder.speed("fast")


screen = Screen()
screen.exitonclick()
