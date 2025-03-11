logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def start():
    
    print("Welcome to the Silent Auction Program!")
    name = input("What is your name? ")
    
    while True:
        try:
            bid = int(input("What is your bid? $"))
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    bidders = {}
    bidders[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    while others == "yes":
        print("\n" * 100)
        name = input("What is your name? ")
    
        while True:
            try:
                bid = int(input("What is your bid? $"))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        bidders[name] = bid
        others = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    else:
        print("\n" * 100)
        print("The bidding has ended.")
    highest_bid = max(bidders.values())
    for char in bidders:
        if bidders[char] == highest_bid:
            print(f"The winner is {char} with a bid of ${highest_bid}")

start()
while True:
    again = input("Would you like to start a new auction? Type 'yes' or 'no'. ").lower()
    while again not in ["yes", "no"]:
        print("Please enter a valid response.")
        again = input("Would you like to start a new auction? Type 'yes' or 'no'. ").lower()
    if again == "yes":
        start()
    else:
        break
print("Goodbye!")
print("Press any key to exit.")