# %%

from turtle import Turtle, Screen, screensize


screen = Screen()

# Drawing screen 500 x 400

screen.setup(width=500, height=400)

# Asking user for input

user_bet = screen.textinput(title="Make your bet",

                            prompt="Which turtle will win the race? Enter a color: ?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

racers = ["eder", "diana", "emilia", "alejo", "alan", "cris"]


# # bulding one turtle

# eder = Turtle(shape="turtle")
# eder.color("red")
# eder.penup()
# eder.goto(-230, -150)
# eder.pendown()

# bulding multiple turtles

y_StartPoint = -150

for racer_index in range(0, 6):
    eder = Turtle(shape="turtle")
    eder.color(colors[racer_index])
    eder.penup()
    eder.goto(-230, y_StartPoint)

    y_StartPoint += 60
    eder.pendown()


screen.exitonclick()


# %%
