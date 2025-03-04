print(r'''
*******************************************************                                    
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
*******************************************************    
''')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
def inicio():    
    print("Bem vindo a jornada do Amuleto Místico!")
    name = input("Qual é o seu nome na história? ")
    print("\nIntrodução")
    print(f"""\nVocê é {name}, um jovem curioso que vive em uma pequena vila cercada por uma floresta densa e misteriosa. 
        Desde criança, você sonha em explorar além dos limites da vila, 
        mas seus pais e os anciãos sempre alertaram sobre os perigos que espreitam na floresta. 
        Um dia, enquanto passeava perto da orla da floresta, 
        você encontra um objeto brilhante parcialmente enterrado no solo. 
        Ao desenterrá-lo, descobre que é um amuleto antigo com inscrições estranhas e um brilho suave.""")
    primeira_escolha(name)

def primeira_escolha(name):
    print("\nO que você faz?")
    print("1. Levar o amuleto para casa e mostrá-lo aos seus pais (Digite: 1)")
    print("2. Guardar o amuleto em segredo e tentar descobrir mais sobre ele por conta própria (Digite: 2)")
    print("3. Deixar o amuleto onde está e esquecer que o encontrou (Digite: 3)")
    
    while True:
        escolha = input("Digite sua escolha (1, 2 ou 3): ")
        if escolha == "1":
            print("\nVocê decide levar o amuleto para casa.")
            caminho_1(name)
            break
        elif escolha == "2":
            print("\nVocê decide guardar o amuleto em segredo.")
            caminho_2(name)
            break
        elif escolha == "3":
            print("\nVocê decide deixar o amuleto onde está.")
            caminho_3(name)
            break
        else:
            print("Por favor, digite apenas 1, 2 ou 3.")
            continue

def caminho_1(name):
    print(f"""{name} leva o amuleto para casa e mostra aos seus pais. Eles ficam pálidos e preocupados. 
          Seu pai explica que o amuleto é um artefato perigoso, ligado a uma antiga lenda sobre uma força maligna. 
          Ele insiste que o objeto deve ser destruído. Mas sua curiosidade fala mais alto. 
          Naquela noite, você foge para a floresta com o amuleto.""")
    print("\nNa floresta, você chega a uma encruzilhada:")
    print("a) Seguir o caminho em direção à luz (Digite: a)")
    print("b) Explorar o caminho mais escuro e sinistro (Digite: b)")
    
    while True:
        escolha = input("Digite sua escolha (a ou b): ")
        if escolha == "a":
            print(f"""\nVocê chega a uma clareira mágica. Um espírito da floresta aparece e explica que o amuleto é uma relíquia sagrada. 
                  Após um treinamento árduo, você usa o amuleto para proteger sua vila, tornando-se um herói.""")
            break
        elif escolha == "b":
            print(f"""\nVocê encontra uma criatura sombria que rouba o amuleto e o trai. 
                  Derrotado, você volta para casa, mas aprende uma lição valiosa sobre cautela.""")
            break
        else:
            print("Por favor, digite apenas 'a' ou 'b'.")
            continue

def caminho_2(name):
    print(f"""{name} guarda o amuleto em segredo. Naquela noite, você sonha com uma voz que fala de ruínas antigas. 
          Ao acordar, você segue para a floresta em busca delas. Lá, encontra uma velha sábia que oferece ajuda.""")
    print("\nO que você faz?")
    print("a) Aceitar a ajuda da velha sábia (Digite: a)")
    print("b) Recusar e continuar sozinho (Digite: b)")
    
    while True:
        escolha = input("Digite sua escolha (a ou b): ")
        if escolha == "a":
            print(f"""\nCom a ajuda da sábia, você chega às ruínas e liberta um herói aprisionado. 
                  Ele agradece e você retorna à vila como salvador.""")
            break
        elif escolha == "b":
            print(f"""\nSozinho, você enfrenta desafios e descobre que o amuleto concede poderes mágicos. 
                  Com eles, você parte para explorar o mundo.""")
            break
        else:
            print("Por favor, digite apenas 'a' ou 'b'.")
            continue

def caminho_3(name):
    print(f"""{name} deixa o amuleto, mas no dia seguinte retorna e vê que ele sumiu. Pegadas levam a uma caverna. 
          Você ouve vozes sobre um 'poder antigo'.""")
    print("\nO que você faz?")
    print("a) Entrar na caverna para investigar (Digite: a)")
    print("b) Voltar para a vila e alertar os anciãos (Digite: b)")
    
    while True:
        escolha = input("Digite sua escolha (a ou b): ")
        if escolha == "a":
            print(f"""\nNa caverna, você encontra exploradores que o veem como o 'escolhido'. 
                  Juntos, descobrem um tesouro que traz prosperidade à vila.""")
            break
        elif escolha == "b":
            print(f"""\nVocê alerta os anciãos, lidera uma expedição e impede que o amuleto caia em mãos erradas. 
                  Você é celebrado como um líder sábio.""")
            break
        else:
            print("Por favor, digite apenas 'a' ou 'b'.")
            continue

# Chama a função para iniciar a história
print("\nFim da aventura. Obrigado por jogar!")
while True:
    inicio()  # Run the calculator
    while True:  # Inner loop to validate the "yes/no" input
        again = input("\nVocê gostaria de ir novamente? (sim/não): ").lower()
        if again in ['sim', 'não']:
            break  # Exit the inner loop if input is valid
        print("Por favor escreva 'sim' ou'não'.")
    if again == 'não':
        print("Até logo!")
        input("Precione enter para fechar o programa...")  # Keeps window open until user presses Enter
        break