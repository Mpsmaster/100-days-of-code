from turtle import Turtle
import random
import time
class Star(Turtle):

    def __init__(self):
        super().__init__()
        for _ in range(100):
            self.shape("circle")
            # self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color("blue")
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            self.goto(random_x, random_y)
            self.screen.update()
            time.sleep(0.1)