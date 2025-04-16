from tkinter import *
import math
import sys
import os


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_counter = None

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_counter)
    canvas.itemconfig(count_label, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    tick.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer_counter
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(count_label, text=f"{minutes}:{seconds}")
    if count > 0:
        timer_counter = window.after(1000, count_down, count - 1)
    else:
        
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            tick.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

canvas_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 112, image=canvas_img)
count_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer.grid(column=1, row=0)

start_b = Button(text="Start", command=start_timer, highlightthickness=0)
start_b.grid(column=0, row=2)

reset_b = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_b.grid(column=2, row=2)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
tick.grid(column=1, row=3)









window.mainloop()