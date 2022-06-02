from turtle import Turtle, Screen
import time


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
    new_snake.penup()
    new_snake.goto(x=x_initial[snake_index], y=0)
    full_snake.append(new_snake)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for seg_num in range(start=2, stop=0, step=-1):
    for seg_num in range(len(full_snake)-1, 0, -1):
        new_x = full_snake[seg_num - 1].xcor()
        new_y = full_snake[seg_num - 1].ycor()
        full_snake[seg_num].goto(new_x, new_y)

    full_snake[0].forward(20)
    full_snake[0].left(50)


screen.exitonclick()
