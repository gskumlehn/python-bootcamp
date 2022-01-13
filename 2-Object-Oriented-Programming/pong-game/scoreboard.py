from turtle import Turtle

YBORDER = 280



class Scoreboard(Turtle):

    # Initiates Scoreboard at top of screen
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.goto(0, 200)
        self.r_score = 0
        self.l_score = 0
        self.write(f'{self.l_score}     {self.r_score}', align='center', font=('Courier', 80, 'normal'))

    # Updates Scoreboard
    def score_update(self):
        self.clear()
        self.write(f'{self.l_score}     {self.r_score}', align='center', font=('Courier', 80, 'normal'))
