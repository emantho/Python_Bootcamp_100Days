# %%
from turtle import Turtle, Screen, screensize

eder = Turtle()
screen = Screen()


def move_forward():
    eder.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

# %%
