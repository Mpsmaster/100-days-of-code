def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    if n2 == 0:  # Check for division by zero
        raise ValueError("Cannot divide by zero!")
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

def start():
    print("Welcome to calculator")
    while True:
        try:
            number1 = float(input("What is the first number? "))
            if number1 == 0:
                print("Please write a number different from 0")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue
        break
    while True:
        math_sign = input("Choose an operation? ")
        if math_sign not in ["+", "-", "/", "*"]:
            print("Please choose one of the four operations")
            continue
        else:
            break
    while True:
        try:
            number2_input = input("What is the second number? ")
            number2 = float(number2_input)  # Convert to float first
            result = operations[math_sign](number1, number2)  # Then try the operation
            break  # If successful, exit the loop
        except ValueError as e:
            if str(e) == "Cannot divide by zero!":
                print("Cannot divide by zero!")
            else:
                print("Please enter a valid number")
            continue
    
    print(f"The result of {number1} {math_sign} {number2} is {result}")
    
    while True:
        keep_result = input(f"If you want another operation with {result} press 'y', if not press 'n'. ").lower()
        if keep_result not in ['y', 'n']:
            print("Please type 'y or 'n.")
            continue
        elif keep_result == "y":
            number1 = result
            should_exit = number_kept(number1)
            if should_exit:
                return
            break
        else:
            break
    
    while True:
        new_op = input("Do you want to make a new operation? 'y' or 'n' ").lower()
        if new_op not in ['y', 'n']:
            print("Please type 'y or 'n.")
            continue
        else:
            if new_op == "y":
                start()
            else:
                print("Goodbye")
                input("Press enter to exit")
                return

def number_kept(number1):
    while True:
        math_sign = input("Choose an operation? ")
        if math_sign not in ["+", "-", "/", "*"]:
            print("Please choose one of the four operations")
            continue
        else:
            break
    while True:
        try:
            number2_input = input("What is the second number? ")
            number2 = float(number2_input)  # Convert to float first
            result = operations[math_sign](number1, number2)  # Then try the operation
            break  # If successful, exit the loop
        except ValueError as e:
            if str(e) == "Cannot divide by zero!":
                print("Cannot divide by zero!")
            else:
                print("Please enter a valid number")
            continue
    
    print(f"The result of {number1} {math_sign} {number2} is {result}")
    
    while True:
        keep_result = input(f"If you want another operation with {result} press 'y', if not press 'n'. ").lower()
        if keep_result not in ['y', 'n']:
            print("Please type 'y or 'n.")
            continue
        elif keep_result == "y":
            number1 = result
            should_exit = number_kept(number1)
            if should_exit:
                return True
            break
        else:
            break
    
    while True:
        new_op = input("Do you want to make a new operation? 'y' or 'n' ").lower()
        if new_op not in ['y', 'n']:
            print("Please type 'y or 'n.")
            continue
        else:
            if new_op == "y":
                start()
            else:
                print("Goodbye")
                input("Press enter to exit")
                return True
    return False

start()