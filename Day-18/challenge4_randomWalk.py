from turtle import Turtle, Screen
import random

eder = Turtle()
eder.shape("turtle")

colors = [
    "dark gray",
    "black",
    "deep sky blue",
    "lime green",
    "firebrick",
    "red",
    "purple",
    "yellow",
]

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
