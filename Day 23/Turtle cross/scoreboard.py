from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        

    def actual_level(self):
        self.hideturtle()
        self.penup()
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def score_up(self):
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        

           