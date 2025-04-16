from tkinter import *
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    length = 12  # You can adjust the length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, END)  # Clear previous password
    password_entry.insert(0, password)  # Insert new password
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    # Check if any field is empty
    if not website or not password:
        return  # Don't save if website or password is empty
    
    # Save to file
    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
    
    # Clear fields (except email)
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    
    # Set focus back to website entry
    website_entry.focus()

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

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "master@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=0, pady=0)

generate_button = Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3, padx=0, pady=0)

window.mainloop()