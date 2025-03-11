def start():
    print("Welcome to the Trivia Challenge!")
    name = input("What’s your name? ")
    score = 0
    questions = {
        "What’s the capital of France?": "france",
        "Which planet is closest to the Sun?": "mercury",
        "How many legs does a spider have?": "8"
    }
    
    for q, correct in questions.items():
        answer = input(f"{q} ").lower()
        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Nope! It’s {correct}.")
    
    print(f"{name}, you scored {score}/{len(questions)}!")
    if input("Play again? (yes/no) ").lower() == "yes":
        start()
    else:
        print("See ya!")

start()