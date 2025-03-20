MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
penny = 0.01
dime = 0.1
nickel = 0.05
quarter = 0.25
stock = resources
profit = 0

def fill_stock():
    resource_name = input("Choose the resource to fill up: water, milk, or coffee? ").lower()
    if resource_name in ["water", "milk", "coffee"]:
        resource_amount = int(input(f"How much {resource_name} would you like to add? "))
        if resource_amount >= 0:
            stock[resource_name] = stock.get(resource_name, 0) + resource_amount
            print(f"Added {resource_amount} to {resource_name}. New total: {stock[resource_name]}.")
        else:
            print("Amount must be non-negative.")
    else:
        print("Invalid resource. Choose water, milk, or coffee.")

def report():
    print(f"Water: {stock['water']} ml")
    print(f"Milk: {stock['milk']} ml")
    print(f"Coffee: {stock['coffee']} g")
    print(f"Profit: ${profit:.2f}")  # Added profit to report

def check_resources(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if stock[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_order(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        stock[item] -= ingredients[item]

def start():
    global profit  # Declare profit as global to modify it
    print("Welcome to the Coffee Machine!")
    order = input("What do you want to order? (espresso/latte/cappuccino) ").lower()
    
    if order == "report":
        report()
        input("Press enter to restart.")
        start()
        return
    
    if order == "refill":
        fill_stock()
        while True:
            add_more = input("Do you want to add more? Type 'y' or 'n': ").lower()
            if add_more == "y":
                fill_stock()
            elif add_more == "n":
                input("Press enter to restart.")
                start()
                return
            else:
                print("Please enter 'y' or 'n'.")

    if order == "off":
        print("Shutting down. Final profit: ${:.2f}".format(profit))
        input("Press enter to exit.")
        return
    
    if order not in MENU:
        print("Sorry, we don't have that drink.")
        input("Press enter to try again.")
        start()
        return
    
    if not check_resources(order):
        input("Press enter to try again.")
        start()
        return
    
    cost = MENU[order]["cost"]
    print(f"The {order} costs ${cost}.")
    print("How are you going to pay?")
    
    try:  # Added error handling for payment inputs
        penny_user = int(input("How many pennies? "))
        dime_user = int(input("How many dimes? "))
        nickel_user = int(input("How many nickels? "))
        quarter_user = int(input("How many quarters? "))
        
        paid_amount = penny_user * penny + dime_user * dime + nickel_user * nickel + quarter_user * quarter
        
        if paid_amount > cost:
            process_order(order)
            print("Your order is being prepared.")
            profit += cost  # Update profit here
            paid_amount -= cost
            print(f"Here is your change: ${paid_amount:.2f}.")
        elif paid_amount == cost:
            process_order(order)
            print("Your order is being prepared.")
            profit += cost  # Update profit here
        else:
            print("Not enough money. Your money is being refunded.")
    except ValueError:
        print("Invalid input. Please enter numbers for payment.")
    
    input("Press enter to continue.")
    start()

start()