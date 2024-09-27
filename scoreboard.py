
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self,):
        self.score += 1
        self.update_score()


    def update_score(self,):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)