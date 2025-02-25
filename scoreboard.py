from turtle import Turtle
ALIGNMENT = 'center'
FONT= ('Courier', 40, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.color('white')
        self.goto(0,240)
        self.write(f'{self.l_score} : {self.r_score}', False, align=ALIGNMENT, font=FONT)

    def r_win(self):
        self.r_score += 1
        self.clear()
        self.write(f'{self.l_score} : {self.r_score}', False, align=ALIGNMENT, font=FONT)

    def l_win(self):
        self.l_score += 1
        self.clear()
        self.write(f'{self.l_score} : {self.r_score}', False, align=ALIGNMENT, font=FONT)

