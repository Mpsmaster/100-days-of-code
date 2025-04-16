from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        website_entry.focus()
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}") 
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()  

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  password_entry.delete(0, END)
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
  password_list = password_letters + password_symbols + password_numbers

  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not password:
        messagebox.showerror(title="Error", message="Please fill in all fields.")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        website_entry.focus()
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
             with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)    
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)


        website_entry.delete(0, END)
        password_entry.delete(0, END)

        website_entry.focus()
        return
    else:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        website_entry.focus()
        return          
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "master@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

add_button = Button(text="Add", width=35, command=save_file)  # Keep width same, but tweak if needed
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=0, pady=0)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3, padx=0, pady=0)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, padx=0, pady=0)






















window.mainloop()