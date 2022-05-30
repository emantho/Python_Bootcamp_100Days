from turtle import Turtle, Screen

# Building up acreen for Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

# Creating Snake body

x_initial = [0, -20, -40]
full_snake = []

for snake_index in range(0, 3):
    new_snake = Turtle("square")
    new_snake.color("white")
    new_snake.speed(5)
    new_snake.penup()
    new_snake.goto(x=x_initial[snake_index], y=0)
    full_snake.append(new_snake)


game_is_on = True

while game_is_on:
    for body in full_snake:
        body.forward(10)


screen.exitonclick()
