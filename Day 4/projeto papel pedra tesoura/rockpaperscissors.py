import random

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
hands = [rock, paper, scissors]
print("Bem vindo ao mestre do papel pedra e tesoura! Você consegue vencê-lo numa melhor de três? " 
    "Vamos ver!")
def inicio():
    
    while True:
        choice = input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura. ")
        print("Você escolheu:")
        if choice in ["0", "1", "2"]:
            print(hands[int(choice)])
            break
        else:
            print("Escolha inválida! Por favor, escolha 0, 1 ou 2.")
    print("Computador escolheu:")
    computer_choice = random.randint(0, 2)
    print(hands[computer_choice])

    computer_choice = str(computer_choice)

    if choice == computer_choice:
        print("Empate!")
    elif choice == "0" and computer_choice == "1":
        print("Você perdeu!")
    elif choice == "0" and computer_choice == "2":
        print("Você ganhou!")
    elif choice == "1" and computer_choice == "0":
        print("Você ganhou!")
    elif choice == "1" and computer_choice == "2":
        print("Você perdeu!")
    elif choice == "2" and computer_choice == "0":
        print("Você perdeu!")
    elif choice == "2" and computer_choice == "1":
        print("Você ganhou!")

inicio()
print("Vamos a segunda rodada!")
inicio()
print("vamos a terceira rodada!")
inicio()
while True:
    play_again = input("Quer jogar novamente? (s/n) ")
    if play_again == "s":
        inicio()
        print("Vamos a segunda rodada!")
        inicio()
        print("vamos a terceira rodada!")
        inicio()
    elif play_again == "n":
        break    
    else:
        print("Escolha inválida! Por favor, escolha s ou n.")
print("Obrigado por jogar!")
print("Pressione Enter para sair")
