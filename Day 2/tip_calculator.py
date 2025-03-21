def calculate_tip():
    print("Welcome to the tip calculator.")

# Get total bill with validation
    while True:
        try:
            total_bill = float(input("What was the total bill? R$ "))
            if total_bill <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

# Get tip percentage with validation
    while True:
        try:
            tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
            if tip_percentage not in [10, 12, 15]:
                print("Please enter 10, 12, or 15.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

# Get number of people with validation
    while True:
        try:
            people = int(input("How many people to split the bill? "))
            if people <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

# Calculate and display results
    total_pay = total_bill * (tip_percentage / 100) + total_bill
    bill_per_person = total_pay / people
    print(f"Total bill: R${total_pay:.2f}. Bill per person: R${bill_per_person:.2f}")
# Main loop to allow multiple calculations
while True:
    calculate_tip()  # Run the calculator
    while True:  # Inner loop to validate the "yes/no" input
        again = input("\nWould you like to calculate another tip? (yes/no): ").lower()
        if again in ['yes', 'no']:
            break  # Exit the inner loop if input is valid
        print("Please enter 'yes' or 'no'.")
    if again == 'no':
        print("Goodbye!")
        input("Press Enter to close the program...")  # Keeps window open until user presses Enter
        break