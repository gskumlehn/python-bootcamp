from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    # Creates list of cars
    def __init__(self):
        super().__init__()
        self.ht()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.chance = 6
        self.yes = [1]

    # Creates cars and appends to car list
    def create_car(self):
        random_chance = randint(1, self.chance)
        for i in self.yes:
            if random_chance == 1:

                car = Turtle('square')
                car.speed('fastest')
                car.setheading(180)
                car.penup()
                car.shapesize(1, 2)
                car.color(choice(COLORS))
                car.goto(300, choice(list(range(-250, 250, 20))))
                self.car_list.append(car)

    # Moves cars forward
    def move(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    # Increases speed at new levels
    def speed_up(self):
        if self.chance == 1:
            self.chance = 6
            new_chance = self.yes[-1] + 1
            self.yes.append(new_chance)
            self.car_speed = STARTING_MOVE_DISTANCE
        else:
            self.car_speed += MOVE_INCREMENT
            self.chance -= 1
