from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

def start():
    while True:
        print("Welcome to the Coffee Machine!")
        options = my_menu.get_items()
        order = input(f"What would you like to order? {options}? ")
        if order == "off":
            return
        elif order == "report":
            my_coffee_maker.report()
            my_money_machine.report()
            input("Press enter to restart.")
            continue
        else:
            choice = my_menu.find_drink(order)
            print(f"Debug: Choice is {choice}")
            available = my_coffee_maker.is_resource_sufficient(choice)
            print(f"Debug: Resources available? {available}")

            if available:  # Line 27 equivalent
                print("Debug: Asking for coins now...")
                paid_money = my_money_machine.process_coins()
                print(f"Debug: Paid money = {paid_money}")
                payment = my_money_machine.make_payment(paid_money)  # Line 28 equivalent
                print(f"Debug: Payment successful? {payment}")

                if payment:
                    my_coffee_maker.make_coffee(choice)  # Assuming this method exists
                    print("Your coffee is being prepared.")
                    input("Thank you for buying, press enter to restart.")
                else:
                    print("Sorry, not enough money. Money refunded.")
                    input("Press enter to restart.")
            else:
                print("Sorry, not enough resources to make that drink.")
                input("Press enter to restart.")

start()