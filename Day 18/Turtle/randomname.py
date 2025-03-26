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
timmy.pensize(5)
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
    timmy.forward(40)
    direction = random.choice([0, 90, 180, 270])
    timmy.setheading(direction)
    
    # Write a name in black (10% chance)
    if random.random() < 0.1:
        timmy.pencolor("black")  # Set color to black for the name
        timmy.write(random.choice(names), font=("Arial", 12, "normal"))
        timmy.pencolor(random_colors())  # Restore the random color for the line
    
    # Randomly turn left or right
    
    
# Set up the screen
screen = Screen()
screen.exitonclick()