from turtle import Turtle, Screen, colormode
import random

# List of colors


# Set up the turtle
timmy = Turtle()
# timmy.pensize(1)
timmy.speed("fastest")  # Fast speed for smoother animation
colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def graph(gap):

    for color in range(int(360 / gap)):
        timmy.color(random_colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

graph(5)
    
    
# Set up the screen
screen = Screen()
screen.exitonclick()