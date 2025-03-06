import random
def inicio():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    
    print("Bem vindo ao mestre do papel pedra e tesoura! Você consegue vencê-lo numa melhor de três? " 
    "Vamos ver!")
    while True:
        choice = input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura. ")
        print("Você escolheu:")
        if choice == "0":
            print(rock)
            break
        elif choice == "1":
            print(paper)
            break
        elif choice == "2":
            print(scissors)
            break
        else:
            print("Escolha inválida! Por favor, escolha 0, 1 ou 2.")
    print("Computador escolheu:")
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    if choice == "0" and computer_choice == 0:
        print("Empate!")
    elif choice == "0" and computer_choice == 1:
        print("Você perdeu!")
    elif choice == "0" and computer_choice == 2:
        print("Você ganhou!")
    elif choice == "1" and computer_choice == 0:
        print("Você ganhou!")
    elif choice == "1" and computer_choice == 1:
        print("Empate!")
    elif choice == "1" and computer_choice == 2:
        print("Você perdeu!")
    elif choice == "2" and computer_choice == 0:
        print("Você perdeu!")
    elif choice == "2" and computer_choice == 1:
        print("Você ganhou!")
    elif choice == "2" and computer_choice == 2:
        print("Empate!")
def inicio2():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    
    print("Vamos a segunda rodada!")
    while True:
        choice = input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura. ")
        print("Você escolheu:")
        if choice == "0":
            print(rock)
            break
        elif choice == "1":
            print(paper)
            break
        elif choice == "2":
            print(scissors)
            break
        else:
            print("Escolha inválida! Por favor, escolha 0, 1 ou 2.")
    print("Computador escolheu:")
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    if choice == "0" and computer_choice == 0:
        print("Empate!")
    elif choice == "0" and computer_choice == 1:
        print("Você perdeu!")
    elif choice == "0" and computer_choice == 2:
        print("Você ganhou!")
    elif choice == "1" and computer_choice == 0:
        print("Você ganhou!")
    elif choice == "1" and computer_choice == 1:
        print("Empate!")
    elif choice == "1" and computer_choice == 2:
        print("Você perdeu!")
    elif choice == "2" and computer_choice == 0:
        print("Você perdeu!")
    elif choice == "2" and computer_choice == 1:
        print("Você ganhou!")
    elif choice == "2" and computer_choice == 2:
        print("Empate!")
def inicio3():
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    
    print("vamos a terceira rodada!")
    while True:
        choice = input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura. ")
        print("Você escolheu:")
        if choice == "0":
            print(rock)
            break
        elif choice == "1":
            print(paper)
            break
        elif choice == "2":
            print(scissors)
            break
        else:
            print("Escolha inválida! Por favor, escolha 0, 1 ou 2.")
    print("Computador escolheu:")
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    if choice == "0" and computer_choice == 0:
        print("Empate!")
    elif choice == "0" and computer_choice == 1:
        print("Você perdeu!")
    elif choice == "0" and computer_choice == 2:
        print("Você ganhou!")
    elif choice == "1" and computer_choice == 0:
        print("Você ganhou!")
    elif choice == "1" and computer_choice == 1:
        print("Empate!")
    elif choice == "1" and computer_choice == 2:
        print("Você perdeu!")
    elif choice == "2" and computer_choice == 0:
        print("Você perdeu!")
    elif choice == "2" and computer_choice == 1:
        print("Você ganhou!")
    elif choice == "2" and computer_choice == 2:
        print("Empate!")        
inicio()
inicio2()
inicio3()
while True:
    play_again = input("Quer jogar novamente? (s/n) ")
    if play_again == "s":
        inicio()
    elif play_again == "n":
        break    
    else:
        print("Escolha inválida! Por favor, escolha s ou n.")
print("Obrigado por jogar!")
print("Pressione Enter para sair")
