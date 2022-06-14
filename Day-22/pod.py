from turtle import Turtle

STARTING_POSITION = [(485, 0), (-485, 0)]
UP = 90
DOWN = 270


class Pod():
    def __init__(self):
        self.positionate_pod()

    def positionate_pod(self):
        for position in STARTING_POSITION:
            self.create_pod(position)

    def create_pod(self, position):
        self.pod = Turtle()
        self.pod.shape("square")
        self.pod.color("white")
        self.pod.penup()
        self.pod.shapesize(stretch_wid=3, stretch_len=0.3, outline=8)
        self.pod.goto(position)

    def move_up(self):
        self.pod.forward(10)
        # self.pod.setheading(UP)

    def move_down(self):
        self.pod.setheading(DOWN)
