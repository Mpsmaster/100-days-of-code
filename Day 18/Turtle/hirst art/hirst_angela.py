import turtle as t
import random

color_list = [(158, 75, 54), (228, 140, 87), (78, 23, 13), (137, 31, 14), (16, 24, 47), (251, 233, 178), (199, 98, 72), (50, 25, 34), (245, 200, 118), (117, 
76, 85), (170, 142, 151), (99, 42, 50), (49, 86, 133), (35, 57, 105), (158, 108, 114), (144, 151, 170), (242, 171, 150), (190, 126, 54), (237, 211, 220), (197, 225, 238), (218, 174, 182), (16, 24, 22), (104, 61, 16), (113, 121, 153), (222, 251, 250), (150, 209, 220), (88, 143, 154), (142, 171, 168), (181, 189, 213), (83, 114, 112)]

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
timmy.goto(0, -150)

for i in range(10):
    for _ in range(10):
        timmy.dot(20, random_colors())
        timmy.forward(50)
    timmy.goto(0, -150 + 50 * (i + 1))



# colors = colorgram.extract('image.jpg', 30)

# rgb_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# print(rgb_list)


screen = t.Screen()
screen.exitonclick()