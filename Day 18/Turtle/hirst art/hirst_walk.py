import turtle as t
import random

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

timmy = t.Turtle()
timmy.speed(0)
t.colormode(255)
timmy.penup()

for _ in range(10001):
    timmy.dot(10, random_colors())
    direction = random.choice([i for i in range(0, 361, 1)])
    timmy.setheading(direction)
    timmy.forward(10)

screen = t.Screen()
screen.exitonclick()