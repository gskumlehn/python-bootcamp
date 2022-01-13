from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # Initiates Scoreboard at top of screen
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.goto(-280, 260)
        self.write(f'Level : {self.score}', font=FONT)

    # Updates score
    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f'Score : {self.score}', font=FONT)

    # Writes out game over at center of screen
    def gameover(self):
        self.goto(0, 0)
        self.write('G A M E  O V E R', align='center', font=FONT)
