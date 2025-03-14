def is_leap_year(year):
    if year % 4 == 0:          # Check if divisible by 4
        if year % 100 == 0:    # Check if divisible by 100
            if year % 400 == 0: # Check if divisible by 400
                return True
            return False
        return True
    return False

# Interactive loop
while True:
    # Get user input
    user_input = input("Enter a year to check if it's a leap year (or 'quit' to exit): ")
    
    # Check if user wants to quit
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    
    # Try to convert input to integer and check if it's a leap year
    try:
        year = int(user_input)
        if is_leap_year(year):
            print(f"{year} is a leap year: True")
        else:
            print(f"{year} is not a leap year: False")
    except ValueError:
        print("Please enter a valid year (number) or 'quit' to exit")