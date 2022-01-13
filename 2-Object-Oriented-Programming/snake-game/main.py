from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, Border
from time import sleep


HEIGHT = 660
WIDTH = 640

# Initiates game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()

# Initiates Screen and connects Keys to methods
screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor('black')
screen.title('SNAKE')
screen.tracer(1)
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

# Plays the game, checking for score updates, collisions with food, border or body, calls for methods necessary
while snake.on:
    screen.update()
    sleep_time = 0.01
    sleep(sleep_time)
    snake.move()
    snake.pos_lst()
    if snake.head.distance(food) < 15:
        food.rand_food()
        snake.grow()
        scoreboard.score_up()
        sleep_time /= scoreboard.score
    if -scoreboard.game_border >= snake.head.xcor() or snake.head.xcor() >= scoreboard.game_border or snake.head.ycor() <= -scoreboard.game_border or snake.head.ycor() >= scoreboard.game_border:
        snake.on = False

scoreboard.gameover()
screen.exitonclick()
