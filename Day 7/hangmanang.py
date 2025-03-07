import random
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
    hiden_word = ""

    for letter in chosen_word:
        hiden_word += "_"
    print("Word to guess: " + hiden_word)
    lives = 6
    game_over = False
    right_guess = [] 
    guessed_letters = []
    print(stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")   
    while not game_over:
        guess = input("Choose a letter. ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z). No numbers, spaces, or special characters!")
            continue

        display = ""

        if guess in guessed_letters:
            print("You have already guessed the letter: " + guess)
            continue
        if guess in chosen_word:
            print("You guessed the letter!")
        for letter in chosen_word:
            if letter == guess:
                display += guess
                right_guess.append(guess)
            elif letter in right_guess:
                display += letter
            else:
                display += "_"
        guessed_letters.append(guess)        
        print("Word to guess: " + display)
        
        if guess not in chosen_word:
            lives -= 1
            print("The letter in not in the hiden word. You lose a life.")
            print(stages[lives])
            print(f"****************************{lives}/6 LIVES LEFT****************************") 
            

            if lives == 0:
                game_over = True
                print("Game over")
                print("The word was: " + chosen_word)
        
        if "_" not in display:
            game_over = True
            print("You win")
start()            

while True:
    play_again = input("Do you want to play again? Type 'yes' or 'no' ").lower()
    if play_again not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'")
        continue
    if play_again == "yes":
        start()
    else:
        break
print("Goodbye!")
input("Press Enter to exit...")        