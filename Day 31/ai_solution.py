from tkinter import *
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# Global variables
current_word = {}
flip_timer = None
data_dict = []
showing_unknown = True  # Track if we're showing unknown words

def load_data():
    global data_dict, showing_unknown
    data_dict = []
    showing_unknown = True
    
    # Load known words, if file exists
    known_words = set()
    if os.path.exists("known_words.csv"):
        known_data = pandas.read_csv("known_words.csv", encoding="utf-8")
        known_words = set(known_data["French"].tolist())
    
    # Load unknown words, if file exists, excluding known words
    if os.path.exists("unknown_words.csv"):
        unknown_data = pandas.read_csv("unknown_words.csv", encoding="utf-8")
        data_dict = [word for word in unknown_data.to_dict(orient="records") if word["French"] not in known_words]
    
    # If no unknown words, load remaining words from french.csv
    if not data_dict:
        showing_unknown = False
        data = pandas.read_csv("french.csv", encoding="utf-8")
        data_dict = [word for word in data.to_dict(orient="records") if word["French"] not in known_words]
        random.shuffle(data_dict)  # Shuffle only remaining words

def load_remaining_words():
    global data_dict, showing_unknown
    # Load remaining words from french.csv, excluding known words
    known_words = set()
    if os.path.exists("known_words.csv"):
        known_data = pandas.read_csv("known_words.csv", encoding="utf-8")
        known_words = set(known_data["French"].tolist())
    
    data = pandas.read_csv("french.csv", encoding="utf-8")
    data_dict = [word for word in data.to_dict(orient="records") if word["French"] not in known_words]
    random.shuffle(data_dict)  # Shuffle remaining words
    showing_unknown = False

def save_known_word(word):
    # Append known word to known_words.csv
    new_data = pandas.DataFrame([word])
    if os.path.exists("known_words.csv"):
        new_data.to_csv("known_words.csv", mode="a", header=False, index=False, encoding="utf-8")
    else:
        new_data.to_csv("known_words.csv", mode="w", header=True, index=False, encoding="utf-8")

def remove_from_unknown(word):
    # Remove word from unknown_words.csv if it exists
    if os.path.exists("unknown_words.csv"):
        unknown_data = pandas.read_csv("unknown_words.csv", encoding="utf-8")
        # Filter out the word
        unknown_data = unknown_data[unknown_data["French"] != word["French"]]
        if not unknown_data.empty:
            unknown_data.to_csv("unknown_words.csv", index=False, encoding="utf-8")
        else:
            # If no words remain, delete the file
            os.remove("unknown_words.csv")

def save_unknown_word(word):
    # Only append if word is not already in unknown_words.csv
    if os.path.exists("unknown_words.csv"):
        unknown_data = pandas.read_csv("unknown_words.csv", encoding="utf-8")
        if word["French"] not in unknown_data["French"].values:
            new_data = pandas.DataFrame([word])
            new_data.to_csv("unknown_words.csv", mode="a", header=False, index=False, encoding="utf-8")
    else:
        new_data = pandas.DataFrame([word])
        new_data.to_csv("unknown_words.csv", mode="w", header=True, index=False, encoding="utf-8")

def random_word():
    global current_word, flip_timer, is_front, data_dict, showing_unknown
    # Cancel any existing timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    
    # If data_dict is empty, load remaining words if showing unknown words
    if not data_dict and showing_unknown:
        load_remaining_words()
    
    # Ensure there are words left to display
    if not data_dict:
        canvas.itemconfig(language_label, text="No more words!")
        canvas.itemconfig(word_label, text="")
        return
    
    # Select the first word from data_dict (maintains unknown word priority)
    current_word = data_dict[0]
    is_front = True
    
    # Show front card and French word
    canvas.itemconfig(card_image, image=canvas_img_front)
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(word_label, text=current_word["French"])
    
    # Schedule flip to back after 3 seconds
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global flip_timer, is_front
    if is_front:
        # Show back of card and English word
        canvas.itemconfig(card_image, image=canvas_img_back)
        canvas.itemconfig(language_label, text="English")
        canvas.itemconfig(word_label, text=current_word["English"])
        is_front = False
    else:
        # Show front of card and French word
        canvas.itemconfig(card_image, image=canvas_img_front)
        canvas.itemconfig(language_label, text="French")
        canvas.itemconfig(word_label, text=current_word["French"])
        is_front = True
    
    # Schedule next flip after 3 seconds
    flip_timer = window.after(3000, flip_card)

def mark_known():
    global current_word, flip_timer, data_dict
    if current_word:
        # Save to known words and remove from data_dict
        save_known_word(current_word)
        remove_from_unknown(current_word)  # Remove from unknown_words.csv
        data_dict.pop(0)  # Remove the current word (first in list)
        # Cancel flip loop and show next word
        if flip_timer is not None:
            window.after_cancel(flip_timer)
        random_word()

def mark_unknown():
    global current_word, flip_timer, data_dict
    if current_word:
        # Save to unknown words only if not already there, then remove from data_dict
        save_unknown_word(current_word)
        data_dict.pop(0)  # Remove the current word (first in list)
        # Cancel flip loop and show next word
        if flip_timer is not None:
            window.after_cancel(flip_timer)
        random_word()

# Set up the window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img_front = PhotoImage(file="card_front.png")
canvas_img_back = PhotoImage(file="card_back.png")
card_image = canvas.create_image(400, 263, image=canvas_img_front)
language_label = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
my_image_wrong = PhotoImage(file="wrong.png")
unknown_button = Button(image=my_image_wrong, highlightthickness=0, command=mark_unknown)
unknown_button.grid(column=0, row=1)

my_image_right = PhotoImage(file="right.png")
known_button = Button(image=my_image_right, highlightthickness=0, command=mark_known)
known_button.grid(column=1, row=1)

# Load data and start the first word
load_data()
random_word()

window.mainloop()