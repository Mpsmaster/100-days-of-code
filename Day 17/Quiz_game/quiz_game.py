import random

def run_quiz():
    while True:  # Main game loop
        # 100 True/False questions about human temperament and behavior
        questions = [
            {"question": "People love being told they’re wrong, it’s their favorite hobby", "correct": "F"},
            {"question": "Everyone secretly enjoys group projects, teamwork makes the dream work", "correct": "F"},
            {"question": "Humans are great at admitting their mistakes, no ego involved", "correct": "F"},
            {"question": "Crying in public is totally a sign of strength, not awkwardness", "correct": "F"},
            {"question": "Everyone handles rejection like a champ, no tears here", "correct": "F"},
            {"question": "People never gossip, they’re too pure for that nonsense", "correct": "F"},
            {"question": "Anger management classes are just for fun, not necessity", "correct": "F"},
            {"question": "Humans always say what they mean, no mixed signals ever", "correct": "F"},
            {"question": "Procrastination is a myth, we’re all super productive", "correct": "F"},
            {"question": "Jealousy? Never heard of it, humans are above that", "correct": "F"},
            {"question": "People love waiting in line, it’s a thrill", "correct": "F"},
            {"question": "Everyone’s a morning person, 6 AM is party time", "correct": "F"},
            {"question": "Shyness is just a fancy way of saying ‘I’m mysterious’", "correct": "F"},
            {"question": "Humans never overreact, they’re chill 24/7", "correct": "F"},
            {"question": "Compliments make everyone uncomfortable, it’s science", "correct": "F"},
            {"question": "We all love confrontation, bring it on!", "correct": "F"},
            {"question": "Nobody’s stubborn, we’re all super flexible", "correct": "F"},
            {"question": "People change their minds easily, no biggie", "correct": "F"},
            {"question": "Laughter is contagious, misery isn’t", "correct": "F"},
            {"question": "Humans never hold grudges, we’re all saints", "correct": "F"},
            {"question": "Being hangry is totally fake, food’s optional", "correct": "F"},
            {"question": "Everyone’s honest all the time, lies are for aliens", "correct": "F"},
            {"question": "Impatience is a virtue, waiting is for losers", "correct": "F"},
            {"question": "We all love criticism, it’s like candy", "correct": "F"},
            {"question": "People never fake smiles, every grin’s legit", "correct": "F"},
            {"question": "Crowds make everyone feel cozy and loved", "correct": "F"},
            {"question": "Humans are pros at letting go of the past", "correct": "F"},
            {"question": "Nobody’s ever passive-aggressive, we’re all direct", "correct": "F"},
            {"question": "Anxiety? Nah, we’re all Zen masters", "correct": "F"},
            {"question": "People love being ignored, it’s flattering", "correct": "F"},
            {"question": "We’re all great listeners, never distracted", "correct": "F"},
            {"question": "Humans never exaggerate, ever, it’s impossible", "correct": "F"},
            {"question": "Everyone’s cool with change, no stress here", "correct": "F"},
            {"question": "Drama follows some people like a loyal puppy", "correct": "T"},
            {"question": "We all secretly judge others, it’s our superpower", "correct": "T"},
            {"question": "People get petty over the dumbest things, shocking", "correct": "T"},
            {"question": "Some humans thrive on chaos, it’s their fuel", "correct": "T"},
            {"question": "Mood swings are a real thing, not just for teens", "correct": "T"},
            {"question": "Humans can be super irrational, big surprise", "correct": "T"},
            {"question": "Some people love playing the victim, it’s an art", "correct": "T"},
            {"question": "We all overthink sometimes, thanks brain", "correct": "T"},
            {"question": "People sulk when they don’t get their way", "correct": "T"},
            {"question": "Humans are weirdly competitive about stupid stuff", "correct": "T"},
            {"question": "Some folks live for attention, it’s their oxygen", "correct": "T"},
            {"question": "We all get cranky without coffee, it’s universal", "correct": "T"},
            {"question": "People ghost others because they’re oh-so-busy", "correct": "T"},
            {"question": "Humans panic over tiny problems, it’s adorable", "correct": "T"},
            {"question": "Some people are just born grumpy, it’s their face’s fault", "correct": "T"},
            {"question": "We all secretly love a good rant session", "correct": "T"},
            # Adding more to reach 100
            {"question": "Everyone’s secretly insecure, even the loud ones", "correct": "T"},
            {"question": "People fake confidence like it’s an Olympic sport", "correct": "T"},
            {"question": "Humans love blaming others, it’s never their fault", "correct": "T"},
            {"question": "We all crave validation, deny it all you want", "correct": "T"},
            {"question": "Some people talk just to hear their own voice", "correct": "T"},
            {"question": "Humans get bored way too easily, it’s pathetic", "correct": "T"},
            {"question": "We all secretly hate being told what to do", "correct": "T"},
            {"question": "People love arguing online, it’s their cardio", "correct": "T"},
            {"question": "Humans obsess over likes, it’s totally healthy", "correct": "T"},
            {"question": "We all pretend we’re fine when we’re not", "correct": "T"},
            {"question": "Some folks can’t handle silence, it’s too spooky", "correct": "T"},
            {"question": "People get salty when they lose, every time", "correct": "T"},
            {"question": "We all secretly love eavesdropping, it’s juicy", "correct": "T"},
            {"question": "Humans flip out when plans change, so dramatic", "correct": "T"},
            {"question": "Some people are loud just to feel important", "correct": "T"},
            {"question": "We all get petty revenge fantasies, admit it", "correct": "T"},
            {"question": "People love showing off, humility’s overrated", "correct": "T"},
            {"question": "Humans freak out over public speaking, it’s cute", "correct": "T"},
            {"question": "We all secretly hate group chats, too much noise", "correct": "T"},
            {"question": "Some folks can’t take a joke, zero chill", "correct": "T"},
            {"question": "People get clingy when they’re lonely, duh", "correct": "T"},
            {"question": "We all secretly love complaining, it’s therapy", "correct": "T"},
            {"question": "Humans overcomplicate everything, it’s their talent", "correct": "T"},
            {"question": "Some people sulk for attention, it’s a classic", "correct": "T"},
            {"question": "We all get annoyed by slow walkers, it’s universal", "correct": "T"},
            {"question": "People love being right, it’s their drug", "correct": "T"},
            {"question": "Humans fake laugh at bad jokes, every time", "correct": "T"},
            {"question": "Some folks can’t say no, it’s their curse", "correct": "T"},
            {"question": "We all get smug when we win, it’s human", "correct": "T"},
            {"question": "People lose it when they’re tired, so fragile", "correct": "T"},
            {"question": "Humans love drama TV because they’re nosy", "correct": "T"},
            {"question": "Some people can’t shut up, it’s a condition", "correct": "T"},
            {"question": "We all secretly hate loud chewers, it’s war", "correct": "T"},
            {"question": "People get weird when they’re hungry, fact", "correct": "T"},
            {"question": "Humans love multitasking, then mess it all up", "correct": "T"},
            {"question": "Some folks thrive on stress, it’s their vibe", "correct": "T"},
            {"question": "We all get petty about parking spots, it’s law", "correct": "T"},
            {"question": "People hate being interrupted, it’s personal", "correct": "T"},
            {"question": "Humans love free stuff, even if it’s junk", "correct": "T"},
            {"question": "Some people cry over spilled milk, literally", "correct": "T"},
            {"question": "We all secretly love winning arguments", "correct": "T"},
            {"question": "People get loud when they’re excited, so extra", "correct": "T"},
            {"question": "Humans hate Mondays, it’s in their DNA", "correct": "T"},
            {"question": "Some folks can’t whisper, they’re just broken", "correct": "T"},
            {"question": "We all get lazy when no one’s watching", "correct": "T"},
            {"question": "People love bragging, modesty’s a lie", "correct": "T"},
            {"question": "Humans freak out over bugs, so brave", "correct": "T"},
            {"question": "Some people live for the spotlight, it’s sad", "correct": "T"},
            {"question": "We all secretly hate long meetings, fact", "correct": "T"},
            {"question": "People get dramatic when they’re sick, oscar-worthy", "correct": "T"},
            {"question": "Humans love gossip, it’s their lifeblood", "correct": "T"}
        ]

        score = 0
        print("\nWelcome to the Most Brilliant True/False Quiz Ever!")
        print("Answer with T (True) or F (False), if you dare to try\n")

        # Shuffle questions, because chaos is fun
        random.shuffle(questions)
        
        # Taking 4 questions, because 100 would melt your tiny mind
        selected_questions = questions[:4]
        total_questions = len(selected_questions)

        for i, q in enumerate(selected_questions, 1):
            print(f"Question {i}: {q['question']}")
            
            while True:
                answer = input("\nYour genius answer (T/F): ").upper()
                if answer in ['T', 'F']:
                    break
                print("Wow, really? Just type T or F, genius")

            # Check answer with maximum sass
            if answer == q["correct"]:
                print("Correct! Shocking you got that right!")
                score += 1
            else:
                print(f"Wrong! Obviously it’s {q['correct']}. Better luck next time, champ")
            print(f"Score (if you can call it that): {score}/{total_questions}\n")

        # Final results with extra sarcasm
        percentage = (score / total_questions) * 100
        print("Quiz over! You survived, somehow!")
        print(f"Final score: {score}/{total_questions} - a true masterpiece")
        print(f"Percentage: {percentage}% - frame-worthy, right?")

        # Sarcastic feedback
        if percentage == 100:
            print("Perfect score! Are you cheating or just secretly a nerd?")
        elif percentage >= 70:
            print("Not terrible! Did you Google that or something?")
        else:
            print("Yikes! Maybe stick to something easier, like napping")

        # Play again prompt
        while True:
            play_again = input("\nWanna try again and prove you’re not a total lost cause? (Y/N): ").upper()
            if play_again in ['Y', 'N']:
                break
            print("It’s Y or N, genius. Try typing one of those")
        
        if play_again == 'N':
            print("Fine, quitter! See ya never!")
            break
        print("Oh, brave soul! Let’s torture you with more questions!")

if __name__ == "__main__":
    run_quiz()