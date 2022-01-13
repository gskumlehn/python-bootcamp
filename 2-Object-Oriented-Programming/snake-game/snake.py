from turtle import Turtle

# Start position and directions
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    # Creates a snake made by 3 Turtle objects, 1 as the head and 2 as the body
    def __init__(self):
        self.on = True
        self.snake_list = []

        for position in START_POSITION:
            self.grow(position)
        self.head = self.snake_list[0]

    # Adds another Turtle to grow body of Snake
    def grow(self, position=None):
        snake = Turtle(shape='square')
        snake.speed(0)
        snake.color('white')
        snake.penup()
        if position is None:
            if self.snake_list[-1].xcor() == self.snake_list[-1].xcor():
                snake.goto(self.snake_list[-1].xcor(), self.snake_list[-1].ycor() - 20)
            elif self.snake_list[-1].ycor() == self.snake_list[-1].ycor():
                snake.goto(self.snake_list[-1].xcor() - 20, self.snake_list[-1].ycor())
        else:
            snake.goto(position)
        self.snake_list.append(snake)

    # Changes direction of Snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Moves Snakes forward
    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            self.snake_list[i].goto(self.snake_list[i - 1].pos())
        self.snake_list[0].forward(20)

    # Creates a position list for the Snake body parts to check collision with Snake head
    def pos_lst(self):
        pos_lst = []
        for snake in self.snake_list[2:]:
            pos_lst.append(snake.pos())
        for position in pos_lst:
            if self.head.distance(position) < 20:
                self.on = False


