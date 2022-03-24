
# importing module turtle
import turtle

# using turtle module from Turtle class
timmy = turtle.Turtle()

# Simplifying this

# importing Turtle class directly from turtle module
from turtle import Turtle, Screen
emi = Turtle()
print(emi)
emi.shape("turtle")
emi.color("blue")
emi.forward(100)
emi.position()

# --- Using objects ---

my_screen = Screen()

# Object > atribute
print(my_screen.canvheight)

# object > method
my_screen.exitonclick()


