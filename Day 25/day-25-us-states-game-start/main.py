import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
turtle.title("U.S. States Game")
turtle.tracer(0)
turtle.penup()

states_data = pd.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
states_x = states_data["x"].to_list()
states_y = states_data["y"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    user_answer = turtle.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="Type the name of a US state:")
    user_answer = user_answer.title()
    if user_answer == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        pd.DataFrame(missing_states).to_csv("missing_states.csv")
        break
    if user_answer in states_list:
        guessed_states.append(user_answer)
        turtle.goto(states_x[states_list.index(user_answer)], states_y[states_list.index(user_answer)])
        turtle.write(user_answer, align="center", font=("Arial", 8, "normal"))
        states_list.remove(user_answer)

