from turtle import Turtle

ALINGMENT = "center"
FONT = ("Courier", 12, 'bold')


class Scoreboard(Turtle):

    def __init__(self, ):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}",
                   move=False, align=ALINGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",
                   move=False, align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
