from turtle import Turtle
import random

COLOR = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# TODO-1 Cars Y available space in screen 250, -250
# TODO-2 Car position must be Random between -250 to 250 with 1 px of space among cars
# TODO-3


class CarManager():

    def __init__(self):
        super().__init__()
        self.cars = []
        # self.create_car()

    def create_car(self):
        if random.randint(1, 5) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLOR))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def reset(self):
        self.cars.clear()
