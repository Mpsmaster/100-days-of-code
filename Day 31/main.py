from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

def random_word():
    data = pandas.read_csv("french.csv", encoding="utf-8")
    data_dict = data.to_dict(orient="records")
    selected_word = random.choice(data_dict)
    french_word = selected_word["French"]
    english_word = selected_word["English"]
    chosen_word = random.choice([french_word, english_word])
    canvas.itemconfig(translation_label, text=chosen_word)
        
       

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas_img = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=canvas_img)
word_label = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
translation_label = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

my_image_wrong = PhotoImage(file="wrong.png")
unknown_button = Button(image=my_image_wrong, highlightthickness=0, command=random_word)
unknown_button.grid(column=0, row=1)

my_image_right = PhotoImage(file="right.png")
known_button = Button(image=my_image_right, highlightthickness=0, command=random_word)
known_button.grid(column=1, row=1)





window.mainloop()