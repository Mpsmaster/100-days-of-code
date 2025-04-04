import tkinter as tk

# def add(*args):
#     total = sum(args)
#     print(f"Total: {total}")




# add(1, 2, 3, 4, 5)

tki = tk.Tk()
tki.title("Getting everything")
tki.minsize(500, 500)
my_label = tk.Label(text="Always hungry for more", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    my_label.config(text=input.get())
my_button = tk.Button(text="Get me", command=button_clicked)
my_button.pack()

input = tk.Entry()
input.pack()










tk.mainloop()