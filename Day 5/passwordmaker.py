import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['#', '$', '%', '&', '@']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? (minimum 2 for at least one uppercase and one lowercase)\n"))
nr_symbols = int(input("How many symbols would you like? (minimum 1)\n"))
nr_numbers = int(input("How many numbers would you like? (minimum 1)\n"))

# Ensure minimum requirements
while True:
    if nr_letters < 2:
        print("Password must have at least one uppercase and one lowercase letter. Please enter at least 2 letters.")
        nr_letters = int(input("How many letters would you like in your password?\n"))
    elif nr_symbols < 1:
        print("Password must have at least one symbol.")
        nr_symbols = int(input("How many symbols would you like?\n"))
    elif nr_numbers < 1:
        print("Password must have at least one number.")
        nr_numbers = int(input("How many numbers would you like?\n"))
    elif nr_letters + nr_symbols + nr_numbers < 8:
        print("Password must have at least 8 characters. Please try again.")
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
    else:
        break

# Create empty list to store password characters
password_list = []

# Add mandatory characters first
password_list.append(random.choice(uppercase))  # At least one uppercase
password_list.append(random.choice(lowercase))  # At least one lowercase
password_list.append(random.choice(symbols))    # At least one symbol
password_list.append(random.choice(numbers))    # At least one number

# Add remaining letters (total letters minus the 2 mandatory ones)
remaining_letters = nr_letters - 2
all_letters = lowercase + uppercase  # Combined list for remaining letters
for char in range(remaining_letters):
    password_list.append(random.choice(all_letters))

# Add remaining symbols (total symbols minus the 1 mandatory one)
for char in range(nr_symbols - 1):
    password_list.append(random.choice(symbols))

# Add remaining numbers (total numbers minus the 1 mandatory one)
for char in range(nr_numbers - 1):
    password_list.append(random.choice(numbers))

# Shuffle the password list to make it more random
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print(f"Your password is: {password}")