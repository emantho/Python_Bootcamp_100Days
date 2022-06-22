from turtle import Turtle

FONT = ["Courier", 18, "bold"]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.goto(-270, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_Scoreboard()

    def game_over(self):
        self.update_Scoreboard()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
