from turtle import Turtle, Screen
import random

colors = [
    "red",      
    "orange",   
    "yellow",   
    "green",   
    "blue",     
    "indigo",   
    "violet"   
]

is_race_on = False
screen = Screen()
user_bet = screen.textinput(
    title="Make your bet.", 
    prompt="Which turtle will get on the finish line first? Choose a color from: red, orange, yellow, green, blue, indigo, violet"
)
screen.setup(500, 500)

turtles = []

for i in range(7):
    players = Turtle("turtle")
    players.color(colors[i])
    players.penup()
    players.goto(-230, -120 + 40 * i)
    turtles.append(players)

if user_bet:
    is_race_on = True    

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You won! The {win_color} turtle won.")
            else:
                print(f"You lost! The {win_color} turtle won.")   
        random_distance = random.randint(0 , 10)
        turtle.forward(random_distance)








screen.exitonclick()