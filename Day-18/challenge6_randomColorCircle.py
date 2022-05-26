from turtle import Turtle, Screen
import random
import turtle

eder = Turtle()
eder.shape("turtle")
turtle.colormode(255)

# TODO: Speed up the turtle when moving
eder.speed(0)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_t = (r, g, b)
    return(color_t)


# TODO: Create a random walk for the turtle

def draw_spirograph(gap):
    direction = 0
    while direction < 360:

        # TODO: Use R,G,B instead color names
        eder.pen(pencolor=random_colors())
        eder.setheading(direction)
        direction += gap
        eder.circle(100)


draw_spirograph(1)


screen = Screen()
screen.exitonclick()
