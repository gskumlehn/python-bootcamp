from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # Creates turtle for player
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed('fast')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    # Moves turtle forward
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Checks if turtle reached the finish line
    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # Resets turtle to starting position
    def reset_player(self):
        self.goto(STARTING_POSITION)
