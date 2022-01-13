from turtle import Screen
from pad import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

HEIGHT = 600
WIDTH = 800

# Initiates game components
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Initiates screen and connects keys to methods
screen = Screen()
screen.bgcolor('black')
screen.setup(height=HEIGHT, width=WIDTH)
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

# Plays game and calls methods
on = True
while on:
    sleep(0.06)
    screen.update()
    ball.bounce_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()
    if ball.xcor() > 370:
        scoreboard.l_score += 1
        ball.reset_ball()
    elif ball.xcor() < -370:
        scoreboard.r_score += 1
        ball.reset_ball()
    scoreboard.score_update()





screen.exitonclick()