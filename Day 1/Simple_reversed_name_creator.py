def reverse_name():
    print("Reverse name creator")
    name = (input("What is your name?"))
    print(name)
    name_reversed = " ".join(word[::-1] for word in name.split()).title()
    print(name_reversed)
while True:
    reverse_name()
    print("\nWould you like to reverse another name?")
    again = input("Enter 'yes' to continue or 'no' to exit: ").lower()
    if again != 'yes':
        print("Goodbye!")
        input("Press Enter to close the program...")  # Keeps window open until user presses Enter
        break