# %%
from turtle import Turtle, Screen, screensize

eder = Turtle()
screen = Screen()


def forward():
    eder.forward(10)


def up():
    eder.setheading(90)


def down():
    eder.setheading(270)


def left():
    eder.setheading(180)


def right():
    eder.setheading(0)


screen.listen()
screen.onkey(key="space", fun=forward)
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.exitonclick()

# %%
