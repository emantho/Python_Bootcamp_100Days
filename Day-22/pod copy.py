from turtle import Turtle

STARTING_POSITION = [350, 0]#, (-485, 0)]
POD_STEP = 20


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
        self.pod.shapesize(stretch_wid=20, stretch_len=100)
        self.pod.right(90)
        self.pod.goto(position)

    def move_up(self):
        self.pod.backward(POD_STEP)
        # self.pod.setheading(UP)

    def move_down(self):
        self.pod.forward(POD_STEP)
