from turtle import Screen, Turtle

ed = Turtle()

for _ in range(15):
    ed.forward(5)
    ed.penup()
    ed.forward(5)
    ed.pendown()

screen = Screen()
screen.exitonclick()