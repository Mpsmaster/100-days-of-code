import random

# List of 20 sarcastic comments for after each guess
SARCASTIC_COMMENTS = [
    "Wow, a genius at work! Not even close.",
    "Oh, bless your heart, you actually tried.",
    "I’ve seen random monkeys do better than that.",
    "Are you guessing or just testing my patience?",
    "Brilliant! ...Said no one ever.",
    "Keep going, you’re only a million miles off.",
    "That was so bad it deserves an award.",
    "You’re making this number cry with those guesses.",
    "I’d say ‘nice try,’ but I don’t like lying.",
    "At this rate, you’ll win... never.",
    "Oh look, another masterpiece of failure!",
    "You’re redefining ‘close enough,’ aren’t you?",
    "My grandma guesses better, and she’s asleep.",
    "That guess was a real knee-slapper—too bad it’s wrong.",
    "Congratulations, you’ve invented a new way to lose!",
    "I’m starting to think you’re trolling me.",
    "Even a broken clock is right more often than you.",
    "You’re so far off, I need a map to find you.",
    "This is why we can’t have nice numbers.",
    "Somewhere, a calculator is weeping for you."
]

def get_difficulty():
    while True:
        level = input("Pick your poison—'easy' or 'hard', hotshot: ").lower()
        if level in ["easy", "hard"]:
            return 10 if level == "easy" else 5
        print("What part of ‘easy’ or ‘hard’ confuses you? Try again.")

def play_game(attempts):
    print(f"You’ve got {attempts} shots to not embarrass yourself.")
    print("I’ve cooked up a number between 1 and 100. Go wild.")
    number = random.randint(1, 100)
    
    while attempts > 0:
        try:
            guess = int(input("Take a wild stab (1-100, or 0 to flee like a coward): "))
            if guess == 0:
                print("Running away already? Pathetic. Bye!")
                return False
            if guess < 1 or guess > 100:
                print("Hello? Earth to genius—keep it between 1 and 100!")
                continue
            
            # Check guess and give feedback
            if guess < number:
                attempts -= 1
                print("Too low, brainiac!")
            elif guess > number:
                attempts -= 1
                print("Too high, skywalker!")
            else:
                print("Well, well, well—look who finally got it! You win, champ!")
                return True
            
            # Print a random sarcastic comment after each wrong guess
            if attempts > 0:
                print(random.choice(SARCASTIC_COMMENTS))
                print(f"You’ve got {attempts} chances left before total humiliation.")
            else:
                print(f"Game over, loser! The number was {number}. Better luck next life.")
                return False
                
        except ValueError:
            print("Numbers, darling, not poetry. Try an actual digit next time.")
    
    return False

def main():
    print("Welcome to the World’s Sassiest Number Guessing Game!")
    print("Prepare to be roasted and maybe—just maybe—win.")
    while True:
        attempts = get_difficulty()
        play_game(attempts)
        
        while True:
            play_again = input("Dare to face the sarcasm again? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            print("It’s a simple ‘yes’ or ‘no,’ not a life crisis. Pick one.")
            
        if play_again == "no":
            print("Thanks for playing, you brave, foolish soul!")
            input("Hit Enter to crawl away.")
            break
        print("\n" * 20)

if __name__ == "__main__":
    main()