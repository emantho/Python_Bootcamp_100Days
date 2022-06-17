from pickle import NEWOBJ_EX
from turtle import Turtle

NORTEAST = 45
NORTWEST = 135
SOUTWEST = 225
SOUTEAST = 315


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        #self.ball = Turtle()
        self.shape("circle")
        self.color("white")
        self.penup()

    def norteast(self):
        self.setheading(NORTEAST)

    def nortwest(self):
        self.setheading(NORTWEST)

    def souteast(self):
        self.setheading(SOUTEAST)

    def soutwest(self):
        self.setheading(SOUTWEST)

    def move(self):

        self.forward(10)
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)
