from turtle import Turtle
X_INITIAL = [0, -20, -40]
SNAKE_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for snake_index in range(0, 3):
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=X_INITIAL[snake_index], y=0)
            self.full_snake.append(new_snake)

    def move(self):
        for seg_num in range(len(self.full_snake)-1, 0, -1):
            new_x = self.full_snake[seg_num - 1].xcor()
            new_y = self.full_snake[seg_num - 1].ycor()
            self.full_snake[seg_num].goto(new_x, new_y)
        self.head.forward(SNAKE_MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def speed(self):
        self.head.speed(0)
