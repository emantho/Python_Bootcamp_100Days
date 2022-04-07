from turtle import Screen, Turtle
import random


ed = Turtle()
ed.shape("turtle")


def move_forw(steps):
    ed.forward(steps)


def move_back(steps):
    ed.right(steps)


def move_rt(angle):
    ed.backward(angle)


def move_lf(angle):
    ed.left(angle)

# TODO: Create a random walk for the turtle


# TODO: Use random color when turtle moves

# TODO: Increment the ticker of the line

# TODO: Speed up the turtle when moving

screen = Screen()
screen.exitonclick()
