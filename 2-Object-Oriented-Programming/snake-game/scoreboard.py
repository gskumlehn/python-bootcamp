from turtle import Turtle

GAME_BOARDER = 290
SCORE_BOARDER = 320
ALIGNMENT = 'center'
FONT_SCORE = ('Arial', 20, 'normal')
FONT_GAMEOVER = ('Arial', 45, 'bold')


class Scoreboard(Turtle):

    # Initiates a Scoreboard, subclass of Turtle, which writes out the score on screen
    def __init__(self):
        super().__init__()
        self.score = 0
        self.game_border = GAME_BOARDER
        self.speed(0)
        self.ht()
        self.penup()
        self.color('white')
        self.goto(0, GAME_BOARDER)
        self.update_score()

    # Uptades Scoreboard
    def update_score(self):
        self.write(f'SCORE      :      {self.score}', align=ALIGNMENT, font=FONT_SCORE)

    # Adds score points and calls update_score method
    def score_up(self):
        self.clear()
        self.score += 1
        self.update_score()

    # Announces end of game in case of collision with body or screen borders
    def gameover(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f'G A M E   O V E R', align=ALIGNMENT, font=FONT_GAMEOVER)


class Border(Turtle):

    # Initiates a Border, subclass of Turtle, which writes out game's borders
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.ht()
        self.penup()
        self.color('white')
        self.goto(-GAME_BOARDER, GAME_BOARDER)
        self.pendown()
        self.goto(-GAME_BOARDER, -GAME_BOARDER)
        self.goto(GAME_BOARDER, -GAME_BOARDER)
        self.goto(GAME_BOARDER, GAME_BOARDER)
        self.goto(-GAME_BOARDER, GAME_BOARDER)
        self.goto(-GAME_BOARDER, SCORE_BOARDER)
        self.goto(GAME_BOARDER, SCORE_BOARDER)
        self.goto(GAME_BOARDER, GAME_BOARDER)
        self.penup()