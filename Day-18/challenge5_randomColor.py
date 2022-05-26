from turtle import Turtle, Screen
import random
import turtle

eder = Turtle()
eder.shape("turtle")
turtle.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_t = (r, g, b)
    return(color_t)


# TODO: Create a random walk for the turtle
direction = [0, 90, 180, 270]
size = 10

for _ in range(100):
    eder.setheading(random.choice(direction))
    eder.forward(30)

# TODO: Use R,G,B instead color names
    eder.pen(pencolor=random_colors(), pensize=size)

# TODO: Increment the ticker of the line 👆

# TODO: Speed up the turtle when moving
    eder.speed("fast")


screen = Screen()
screen.exitonclick()
