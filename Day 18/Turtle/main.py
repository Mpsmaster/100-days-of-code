from turtle import Turtle, Screen, colormode
import random

# tim = Turtle()
# tim.shape("turtle")
# tim.color("blue2")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
"""In this code, turtle will draw a square"""


# timmy = Turtle()
# timmy.speed(1)
# timmy.shape("turtle")
# timmy.color("blue2")

# for _ in range(50):
#     timmy.pendown()
#     timmy.forward(5)
#     timmy.penup()
#     timmy.forward(5)
#     """In this code, turtle will draw a dashed line"""

timmy = Turtle()
timmy.speed(0)
timmy.shape("turtle")
timmy.color("blue2")
colormode(255)
timmy.penup()
timmy.goto(0, 350)
timmy.pendown()

# for _ in range(3):
#     timmy.forward(100)
#     timmy.right(120)


# for _ in range(4):
#     timmy.forward(100)
#     timmy.color("chartreuse")
#     timmy.right(90)

# timmy.color("blue2")

# for _ in range(5):
#     timmy.forward(100)
#     timmy.color("DarkOrchid")
#     timmy.right(72)    

# timmy.color("blue2")

# for _ in range(6):
#     timmy.forward(100)
#     timmy.color("green")
#     timmy.right(60)  

#     timmy.color("blue2")

# for _ in range(7):
#     timmy.forward(100)
#     timmy.color("red")
#     timmy.right(51.4) 

# timmy.color("blue2")

# for _ in range(8):
#     timmy.forward(100)
#     timmy.color("orange")
#     timmy.right(45) 

# timmy.color("blue2")

# for _ in range(9):
#     timmy.forward(100)
#     timmy.color("yellow")
#     timmy.right(40) 

# timmy.color("blue2")

# for _ in range(10):
#     timmy.forward(100)
#     timmy.color("black")
#     timmy.right(36) 

colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "cyan",
    "magenta",
    "lime",
    "teal",
    "indigo",
    "violet",
    "gray",
    "black",
    "gold",
    "silver",
    "olive"
]

def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_form(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
for all_forms in range(3, 23):
    timmy.color(random_colors())
    draw_form(all_forms)

screen = Screen()
screen.exitonclick()
