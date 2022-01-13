from turtle import Turtle
from random import choice


CORDLIST = list(range(-300 + 20, 300, 20))

class Food(Turtle):

    # Creates a Food object to be eaten by Snake, Food is a subclass of Turtle
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.speed(0)
        self.color('CornflowerBlue')
        self.shapesize(0.5, 0.5)
        self.penup()
        self.goto(choice(CORDLIST), choice(CORDLIST))

    # Randomizes Food location after collision with Snake head (eaten)
    def rand_food(self):
        self.goto(choice(CORDLIST), choice(CORDLIST))
