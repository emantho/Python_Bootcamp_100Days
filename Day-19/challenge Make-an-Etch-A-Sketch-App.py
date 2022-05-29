# %%
from turtle import Turtle, Screen, screensize

eder = Turtle()
screen = Screen()


def move_forward():
    eder.forward(10)


def move_backward():
    eder.backward(10)


def move_left():
    eder.left(5)


def move_right():
    eder.right(5)


def clear():
    eder.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

# %%
