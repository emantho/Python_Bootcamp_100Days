from turtle import Turtle


class Ball():
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.shapesize(stretch_wid=1, stretch_len=1, outline=8)
