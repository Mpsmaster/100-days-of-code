from turtle import Turtle, Screen, colormode
import random

# List of colors
colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown",
    "cyan", "magenta", "lime", "teal", "indigo", "violet", "gray", "black",
    "gold", "silver", "olive"
]

# List of random names
names = [
    "Alice", "Bob", "Charlie", "Daisy", "Eve", "Frank", "Grace", "Hank",
    "Ivy", "Jack", "Kara", "Leo", "Mila", "Nina", "Omar", "Pia", "Quinn",
    "Rose", "Sam", "Tina"
]

# Set up the turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(2)
timmy.speed("fastest")  # Fast speed for smoother animation
colormode(255)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Random walk with names
for _ in range(1001):
    # Set a random color for the line
    timmy.color(random_colors())
    timmy.forward(10)
    direction = random.choice([i for i in range(0, 361, 1)])
    timmy.setheading(direction)

    












screen = Screen()
screen.exitonclick()