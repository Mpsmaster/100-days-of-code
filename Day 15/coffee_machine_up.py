from enum import Enum
from typing import Dict

# Constants
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

COINS = {"penny": 0.01, "nickel": 0.05, "dime": 0.10, "quarter": 0.25}

INITIAL_STOCK = {"water": 300, "milk": 200, "coffee": 100}

VALID_RESOURCES = {"water", "milk", "coffee"}

# Action commands
class Action(Enum):
    ORDER = "order"
    REPORT = "report"
    REFILL = "refill"
    OFF = "off"

# Coffee Machine class to encapsulate state and behavior
class CoffeeMachine:
    def __init__(self):
        self.stock = INITIAL_STOCK.copy()
        self.profit = 0.0

    def report(self) -> None:
        """Display current stock and profit."""
        print("\nCurrent Status:")
        for resource, amount in self.stock.items():
            unit = "ml" if resource in {"water", "milk"} else "g"
            print(f"{resource.capitalize()}: {amount}{unit}")
        print(f"Profit: ${self.profit:.2f}")

    def has_enough_resources(self, drink: str) -> bool:
        """Check if there are enough ingredients for the drink."""
        ingredients = MENU[drink]["ingredients"]
        for resource, required in ingredients.items():
            if self.stock.get(resource, 0) < required:
                print(f"Sorry, not enough {resource}.")
                return False
        return True

    def deduct_resources(self, drink: str) -> None:
        """Deduct ingredients from stock after a successful order."""
        ingredients = MENU[drink]["ingredients"]
        for resource, amount in ingredients.items():
            self.stock[resource] -= amount

    def refill_stock(self) -> None:
        """Refill a chosen resource."""
        while True:
            resource = input("Choose resource to refill (water/milk/coffee): ").lower()
            if resource not in VALID_RESOURCES:
                print("Invalid resource. Choose water, milk, or coffee.")
                continue
            amount = self._get_positive_int(f"How much {resource} to add? ")
            self.stock[resource] = self.stock.get(resource, 0) + amount
            print(f"Added {amount} to {resource}. New total: {self.stock[resource]}.")
            if input("Add more? (y/n): ").lower() != "y":
                break

    def process_payment(self, cost: float) -> bool:
        """Handle payment and return True if sufficient."""
        print(f"Cost: ${cost:.2f}. Please insert coins:")
        payment = 0.0
        for coin, value in COINS.items():
            count = self._get_positive_int(f"How many {coin}s? ")
            payment += count * value
        if payment < cost:
            print("Insufficient payment. Money refunded.")
            return False
        self.profit += cost
        change = payment - cost
        if change > 0:
            print(f"Payment accepted. Change: ${change:.2f}")
        return True

    def _get_positive_int(self, prompt: str) -> int:
        """Helper to get a non-negative integer from user input."""
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("Please enter a non-negative number.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self) -> None:
        """Main loop to run the coffee machine."""
        print("Welcome to the Coffee Machine!")
        while True:
            action = input("Order (drink name), report, refill, or off: ").lower()

            if action == Action.REPORT.value:
                self.report()
            elif action == Action.REFILL.value:
                self.refill_stock()
            elif action == Action.OFF.value:
                print(f"Shutting down. Final profit: ${self.profit:.2f}")
                break
            elif action not in MENU:
                print("Invalid option. Try again.")
            else:
                if self.has_enough_resources(action):
                    cost = MENU[action]["cost"]
                    if self.process_payment(cost):
                        self.deduct_resources(action)
                        print(f"Enjoy your {action}!")
            input("\nPress enter to continue...")

# Start the machine
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()