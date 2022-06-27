from turtle import Turtle

ALINGMENT = "center"
FONT = ("Courier", 12, 'bold')

# Scoreboard modified to track high score
# TODO 1 - Add a High_score variable
# TODO 2 - Modifi game_over function to reset game
# TODO 3 - write a file with high score value


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high-score.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}",
                   move=False, align=ALINGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER",
    #                move=False, align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
