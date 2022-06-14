from turtle import Turtle

POD_STEP = 20

class Pod(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.shape("square")
        # self.color("white")
        # self.penup()
        # self.shapesize(stretch_wid=5, stretch_len=1)
        # self.goto(position)
        self.create_pod(position)


    def create_pod(self,position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        

    def move_up(self):
        new_y = self.ycor() + POD_STEP
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - POD_STEP
        self.goto(self.xcor(), new_y)
