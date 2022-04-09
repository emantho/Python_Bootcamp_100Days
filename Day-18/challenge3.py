# Draw a triangle, square, pentagon, hexagon, heptagon
# octagon, nonagon, and decagon

# angle is given by formule = 360° / shape size
# example: 360 / 4 = 90 or 360 / 5 = 72

from turtle import Turtle, Screen
import random

eder = Turtle()


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


def draw_shape(num_angles):
    angles = 3
    while True:
        giro_Angle = 360 / angles
        eder.color(random.choice(colors))
        for i in range(angles):
            eder.forward(50)
            eder.rt(giro_Angle)
        angles += 1
        if angles == num_angles:
            break


draw_shape(20)

screen = Screen()
screen.exitonclick()
