import random

logo = r"""
 _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/  											 
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def start(high_score):
    print(logo)
    print("Welcome to the Higher Lower Game!")
    print(f"Current High Score: {high_score}")
    print("Guess which topic has more searches on Google!")
    
    # Updated data with top 100 Google search topics
    data = [
        {'name': 'YouTube', 'searches': 361.6},
        {'name': 'Facebook', 'searches': 144.5},
        {'name': 'Amazon', 'searches': 120.3},
        {'name': 'Google', 'searches': 100.2},
        {'name': 'Weather', 'searches': 81.0},
        {'name': 'TikTok', 'searches': 74.5},
        {'name': 'Instagram', 'searches': 60.8},
        {'name': 'Netflix', 'searches': 50.1},
        {'name': 'Gmail', 'searches': 45.7},
        {'name': 'Wordle', 'searches': 40.3},
        {'name': 'Twitter', 'searches': 35.6},
        {'name': 'WhatsApp', 'searches': 33.4},
        {'name': 'NBA', 'searches': 30.5},
        {'name': 'eBay', 'searches': 28.9},
        {'name': 'U.S. Election', 'searches': 25.0},
        {'name': 'Copa América', 'searches': 22.7},
        {'name': 'Olympics', 'searches': 20.8},
        {'name': 'Donald Trump', 'searches': 18.5},
        {'name': 'Taylor Swift', 'searches': 17.2},
        {'name': 'ChatGPT', 'searches': 15.9},
        {'name': 'Walmart', 'searches': 14.8},
        {'name': 'Cricket World Cup', 'searches': 14.5},
        {'name': 'Apple', 'searches': 14.2},
        {'name': 'Tesla', 'searches': 13.9},
        {'name': 'BBC News', 'searches': 13.4},
        {'name': 'Premier League', 'searches': 13.0},
        {'name': 'Microsoft', 'searches': 12.7},
        {'name': 'PayPal', 'searches': 12.4},
        {'name': 'Spotify', 'searches': 12.1},
        {'name': 'LinkedIn', 'searches': 11.8},
        {'name': 'Pornhub', 'searches': 11.5},
        {'name': 'Yahoo', 'searches': 11.2},
        {'name': 'Hotmail', 'searches': 10.9},
        {'name': 'Samsung', 'searches': 10.6},
        {'name': 'Reddit', 'searches': 10.3},
        {'name': 'Target', 'searches': 10.0},
        {'name': 'Elon Musk', 'searches': 9.7},
        {'name': 'NFL', 'searches': 9.4},
        {'name': 'Disney+', 'searches': 9.1},
        {'name': 'Zoom', 'searches': 8.8},
        {'name': 'Canva', 'searches': 8.5},
        {'name': 'Wikipedia', 'searches': 8.2},
        {'name': 'Airbnb', 'searches': 7.9},
        {'name': 'Roblox', 'searches': 7.6},
        {'name': 'Fortnite', 'searches': 7.3},
        {'name': 'Cristiano Ronaldo', 'searches': 7.0},
        {'name': 'McDonalds', 'searches': 6.7},
        {'name': 'Bitcoin', 'searches': 6.4},
        {'name': 'Uber', 'searches': 6.1},
        {'name': 'World Cup', 'searches': 5.9},
        {'name': 'Kamala Harris', 'searches': 5.6},
        {'name': 'CNN', 'searches': 5.4},
        {'name': 'Snapchat', 'searches': 5.2},
        {'name': 'X', 'searches': 5.0},
        {'name': 'Pepsi', 'searches': 4.8},
        {'name': 'Adidas', 'searches': 4.6},
        {'name': 'Nike', 'searches': 4.4},
        {'name': 'Hulu', 'searches': 4.2},
        {'name': 'Translate', 'searches': 4.0},
        {'name': 'iPhone', 'searches': 3.8},
        {'name': 'Shein', 'searches': 3.6},
        {'name': 'Fox News', 'searches': 3.4},
        {'name': 'Discord', 'searches': 3.2},
        {'name': 'Barack Obama', 'searches': 3.0},
        {'name': 'Costco', 'searches': 2.9},
        {'name': 'Grammy Awards', 'searches': 2.8},
        {'name': 'Harry Potter', 'searches': 2.7},
        {'name': 'Kendrick Lamar', 'searches': 2.6},
        {'name': 'Super Bowl', 'searches': 2.5},
        {'name': 'Beyoncé', 'searches': 2.4},
        {'name': 'Etsy', 'searches': 2.3},
        {'name': 'Coronavirus', 'searches': 2.2},
        {'name': 'PlayStation', 'searches': 2.1},
        {'name': 'Xbox', 'searches': 2.0},
        {'name': 'Climate Change', 'searches': 1.9},
        {'name': 'Lionel Messi', 'searches': 1.8},
        {'name': 'SpaceX', 'searches': 1.7},
        {'name': 'Dua Lipa', 'searches': 1.6},
        {'name': 'Instagram Reels', 'searches': 1.5},
        {'name': 'Amazon Prime', 'searches': 1.4}
    ]
    
    # Initial selection with check for different items
    google_search1 = random.choice(data)
    google_search2 = random.choice(data)
    while google_search1 == google_search2:  # Keep picking until they're different
        google_search2 = random.choice(data)
    
    data_display1 = google_search1['name']
    data_display2 = google_search2['name']
    print(f"{data_display1} is number 1")
    print(vs)
    print(f"{data_display2} is number 2")
    score = 0
    
    while True:
        try:
            user_choice = int(input("Who do you think has more searches? Type '1' or '2': "))
            if user_choice not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Please enter 1 or 2")
            continue
        
        if user_choice == 1:
            if google_search1['searches'] > google_search2['searches']:
                print("You are correct!")
                print(f"{google_search1['name']} had {google_search1['searches']} million searches")
                print(f"{google_search2['name']} had {google_search2['searches']} million searches")
                score += 1
                print(f"Your current score is: {score}")
            else:
                print("You are wrong!")
                print(f"{google_search1['name']} had {google_search1['searches']} million searches")
                print(f"{google_search2['name']} had {google_search2['searches']} million searches")
                print(f"Your final score was: {score}")
                break
        elif user_choice == 2:
            if google_search2['searches'] > google_search1['searches']:
                print("You are correct!")
                print(f"{google_search1['name']} had {google_search1['searches']} million searches")
                print(f"{google_search2['name']} had {google_search2['searches']} million searches")
                score += 1
                print(f"Your current score is: {score}")
            else:
                print("You are wrong!")
                print(f"{google_search1['name']} had {google_search1['searches']} million searches")
                print(f"{google_search2['name']} had {google_search2['searches']} million searches")
                print(f"Your final score was: {score}")
                break
        
        # Pick new topics for the next round with check for different items
        google_search1 = random.choice(data)
        google_search2 = random.choice(data)
        while google_search1 == google_search2:  # Keep picking until they're different
            google_search2 = random.choice(data)
        data_display1 = google_search1['name']
        data_display2 = google_search2['name']
        print(f"{data_display1} is number 1")
        print(vs)
        print(f"{data_display2} is number 2")
    
    return max(score, high_score)

high_score = 0
high_score = start(high_score)

while True:
    play_again = input("Do you want to play again? Type 'y' for yes and 'n' for no: ").lower()
    if play_again not in ["y", "n"]:
        print("Please type 'y' or 'n'.")
    else:
        if play_again == "y":
            high_score = start(high_score)
        else:
            print(f"Goodbye! Your highest score was: {high_score}")
            input("Press enter to exit")
            break