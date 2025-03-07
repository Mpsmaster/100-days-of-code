import random

# Hangman stages (unchanged)
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# ASCII art (unchanged)
print(r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

def start():
    print("Welcome to the Hangman game!")
    input("Press Enter to start the game...")
    
    # Word list (unchanged)
    word_list = [
        "algorithm", "binary", "bytecode", "cache", "compiler", "debug", "encryption", "firewall", "git", "hash",
        "integer", "javascript", "kernel", "loop", "matrix", "namespace", "opcode", "pixel", "query", "regex",
        "server", "thread", "unicode", "vector", "widget", "xml", "yaml", "zip", "array", "boolean",
        "circuit", "daemon", "ethernet", "firmware", "gizmo", "heuristic", "interface", "joystick", "kilobyte", "logic",
        "macro", "network", "octet", "packet", "quantum", "router", "script", "syntax", "terminal", "upload",
        "virtual", "wireless", "xenon", "yottabyte", "zombie", "avatar", "blaster", "cyberpunk", "droid", "energy",
        "forcefield", "galaxy", "hyperdrive", "impulse", "jedi", "klingon", "laser", "mech", "nebula", "orbital",
        "photon", "reactor", "shield", "stargate", "teleport", "vortex", "warp", "xray", "android", "bandwidth",
        "cosplay", "dungeon", "elf", "fandom", "goblin", "hitpoints", "inventory", "mana", "noob", "overclock",
        "polygon", "render", "spawn", "texture", "unlock", "voxel", "wizard", "zeroday", "geek", "nerd"
    ]
    
    chosen_word = random.choice(word_list)
    hidden_word = "_" * len(chosen_word)  # Simplified initialization
    print("Word to guess: " + hidden_word)
    lives = 6
    game_over = False
    correct_guesses = set()  # Use set instead of list
    guessed_letters = set()  # Use set instead of list
    print(stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    while not game_over:
        guess = input("Choose a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z). No numbers, spaces, or special characters!")
            continue

        # Check for repeated guesses
        if guess in guessed_letters:
            print("You have already guessed the letter: " + guess)
            continue

        guessed_letters.add(guess)  # Add guess to set

        # Handle correct guess
        if guess in chosen_word:
            print(f"You guessed the letter '{guess}' correctly!")
            correct_guesses.add(guess)
        # Handle incorrect guess
        else:
            lives -= 1
            print("The letter is not in the hidden word. You lose a life.")
            print(stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************")
            if lives == 0:
                game_over = True
                print("Game over")
                print("The word was: " + chosen_word)

        # Update and display game state only if game isn't over
        if not game_over:
            display = ""
            for letter in chosen_word:
                if letter in correct_guesses:
                    display += letter
                else:
                    display += "_"
            print("Word to guess: " + display)
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))
            
            # Check for win
            if "_" not in display:
                game_over = True
                print("You win")

start()

# Play again loop (unchanged)
while True:
    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'")
        continue
    if play_again == "yes":
        start()
    else:
        break
print("Goodbye!")
input("Press Enter to exit...")