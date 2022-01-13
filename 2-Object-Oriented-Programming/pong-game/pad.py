from turtle import Turtle

XBORDER = 350
YBORDER = 250
UP = 90
DOWN = 270


class Paddle(Turtle):

    # Creates a paddle shape and sends to location
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.shapesize(1, 5)
        self.goto(position)
        self.setheading(UP)

    # Movements for the paddle
    def up(self):
        self.goto(self.xcor(),self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(),self.ycor() - 20)