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
            my_money_machine. report()
            input("Press enter to restart.")
            continue
        else:
            choice = my_menu.find_drink(order)
        if my_coffee_maker.is_resource_sufficient(choice):
        
            payment = my_money_machine.make_payment(choice.cost)
        else:
            continue    
            
        if payment == False:
            continue
        else:
            print("Your coffee is being prepared.")
            my_coffee_maker.make_coffee(choice)
            input("Thank you for buying, press enter to restart")
            continue
start()       