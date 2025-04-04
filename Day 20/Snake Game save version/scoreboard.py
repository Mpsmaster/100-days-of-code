from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 24, "normal"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=(FONT))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=(FONT))   

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.update_score()

            
