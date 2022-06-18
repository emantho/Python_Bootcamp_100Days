from turtle import Turtle

FONT = ["Courier", 18, "normal"]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_Scoreboard()
