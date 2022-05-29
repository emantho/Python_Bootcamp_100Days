# %%

from turtle import Turtle, Screen, screensize
import random

is_race_on = False
screen = Screen()

# Drawing screen 500 x 400

screen.setup(width=500, height=400)

# Asking user for input

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -90, -30, 30, 90, 150]
racers = []

# bulding multiple turtles

for racer_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[racer_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[racer_index])
    racers.append(new_turtle)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ?")

if user_bet:
    is_race_on = True

while is_race_on:

    for racer in racers:
        if racer.xcor() > 220:
            is_race_on = False

            if racer.pencolor() == user_bet:
                print(
                    f"You've Won! The turtle {racer.pencolor()} won the race")

            else:
                print(
                    f"You've lost! The turtle {racer.pencolor()} won the race")

        turtle_movement = random.randint(0, 10)
        racer.forward(turtle_movement)


screen.exitonclick()


# %%
