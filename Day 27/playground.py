import tkinter as tk

# def add(*args):
#     total = sum(args)
#     print(f"Total: {total}")




# add(1, 2, 3, 4, 5)

tki = tk.Tk()
tki.title("Getting everything")
tki.minsize(500, 500)
tki.config(padx=20, pady=20)

my_label = tk.Label(text="Always hungry for more", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_label.config(text=input.get())
my_button = tk.Button(text="Get me", command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = tk.Button(text="More money, abundance, everything")
my_button2.grid(column=2, row=0)

input = tk.Entry()
input.grid(column=4, row=3)











tk.mainloop()