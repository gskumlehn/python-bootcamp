from turtle import Turtle

SPEED = 10
class Ball(Turtle):

    # Creates Ball in center of screen
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white', 'white')
        self.penup()
        self.x = SPEED
        self.y = SPEED

    # Defines method to change direction in case of collision with borders
    def bounce_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.y *= -1
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    # Defines method to change direction in case of collision with paddle
    def bounce_paddle(self):
        self.x *= -1

    # Resets ball location in case of point
    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_paddle()




