import random
logo = r'''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/ 
                      '''
print(logo)
print("Bem-vindo ao Jogo de Blackjack, parceiro!")
print("Quer aprender a jogar ou já quer sair apostando?")
resposta = input("Digite 's' pra aprender ou 'n' pra jogar direto: ").lower()
tutorial = resposta == 's'  # Define se o modo tutorial tá ativo

if tutorial:
    print("\n=== Tutorial Rápido de Blackjack - A Festa das Cartas! ===")
    print("1. O objetivo é chegar o mais perto de 21 pontos sem passar, ou 'estourar'. Se estourar, já era!")
    print("2. Você começa com 2 cartas e pode pedir mais ('s') ou parar ('n').")
    print("3. O Ás (11) é um coringa: vira 1 se você passar de 21. Esperto, né?")
    print("4. Se suas 2 primeiras cartas somarem 21, é BLACKJACK! Vitória na hora!")
    print("5. O computador (seu rival) joga depois e precisa chegar a pelo menos 17.")
    print("6. Quem tiver mais pontos sem estourar ganha. Simples e emocionante!")
    print("\nPronto pra arrasar? Vamos lá!")
    input("Pressione Enter pra começar a bagunça!")
else:
    print("Beleza, você já é craque! Vamos direto pro jogo!")
    input("Pressione Enter pra começar a farra!")

def pega_carta():
    """Pega uma carta aleatória do baralho, tipo mágica!"""
    carta = random.choice(cartas)
    return carta

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # O baralho tá pronto!
suas_cartas = []
cartas_computador = []

def calcula_pontos(cartas):
    """Calcula seus pontos com base nas cartas. Vamos somar essa festa!"""
    if sum(cartas) == 21 and len(cartas) == 2:
        return "Blackjack"  # Olha só, você é o rei da festa!
    if 11 in cartas and sum(cartas) > 21:
        cartas.remove(11)  # Tchau, Ás grande!
        cartas.append(1)   # Oi, Ás pequeno!
    return sum(cartas)

def comeca_jogo():
    pega_carta()  # Só pra aquecer o baralho, hehe!
    for _ in range(2):
        suas_cartas.append(pega_carta())
        cartas_computador.append(pega_carta())
    
    print(f"Sua mão: {suas_cartas}, pontos atuais: {calcula_pontos(suas_cartas)}")
    print(f"Primeira carta do computador: {cartas_computador[0]}")
    if tutorial:
        print("(Tutorial: Você ganhou 2 cartas pra começar! O objetivo é ficar perto de 21 sem passar.)")
        print("(Tutorial: O computador também pegou 2, mas só mostra uma por enquanto. Mistério!)")
    
    quer_carta = True
    while quer_carta:
        if calcula_pontos(suas_cartas) == "Blackjack":
            print("Você ganhou com um BLACKJACK! Tá muito chique!")
            if tutorial:
                print("(Tutorial: BLACKJACK! Suas 2 cartas somaram 21 direto. Vitória instantânea!)")
            quer_carta = False
        else:
            escolha = input("Quer mais uma carta? 's' pra sim, 'n' pra parar: ").lower()
            if tutorial:
                print("(Tutorial: 's' pega mais uma carta, 'n' deixa como está e passa pro computador.)")
            if escolha not in ["s", "n"]:
                print("Eita, só vale 's' ou 'n', hein! Tenta de novo!")
                continue
            if escolha == "s":
                suas_cartas.append(pega_carta())
                print(f"Sua mão: {suas_cartas}, pontos atuais: {calcula_pontos(suas_cartas)}")
                if tutorial:
                    print("(Tutorial: Nova carta na mão! Veja se ainda tá abaixo de 21 pra não estourar.)")
                if calcula_pontos(suas_cartas) == 21 and calcula_pontos(cartas_computador) == 21:
                    print("Empate danado! Vocês dois chegaram a 21!")
                    if tutorial:
                        print("(Tutorial: Os dois fizeram 21! Isso é raro, acabou em empate.)")
                    quer_carta = False
                    return
                elif calcula_pontos(suas_cartas) == 21:
                    print("Você fez 21! Vitória na raça!")
                    if tutorial:
                        print("(Tutorial: 21 exatos! Você ganhou sem estourar, parabéns!)")
                    quer_carta = False
                    return
                elif calcula_pontos(suas_cartas) > 21:
                    print("Oops, estourou! Perdeu, mas foi quase, hein!")
                    if tutorial:
                        print("(Tutorial: Passou de 21? Isso é 'estourar'. Fim de jogo pra você dessa vez.)")
                    quer_carta = False
                    return
                elif calcula_pontos(cartas_computador) > 21:
                    print("O computador estourou! Você ganhou, parabéns!")
                    if tutorial:
                        print("(Tutorial: O computador passou de 21 depois. Você ganhou por padrão!)")
                    quer_carta = False
                    return
            else:
                quer_carta = False
                if tutorial:
                    print("(Tutorial: Você parou! Agora o computador joga até pelo menos 17 pontos.)")
    
    pontos_computador = calcula_pontos(cartas_computador)
    while pontos_computador < 17:
        cartas_computador.append(pega_carta())
        pontos_computador = calcula_pontos(cartas_computador)
        if tutorial:
            print("(Tutorial: O computador pegou mais cartas pra chegar a 17 ou mais. Vamos ver no que dá!)")
    
    print(f"Sua mão final: {suas_cartas}, pontos finais: {calcula_pontos(suas_cartas)}")
    print(f"Mão final do computador: {cartas_computador}, pontos finais: {pontos_computador}")
    if tutorial:
        print("(Tutorial: Hora da verdade! Vamos comparar os pontos pra ver quem ganha.)")
    
    if calcula_pontos(suas_cartas) > 21:
        print("Você estourou, que pena! Perdeu dessa vez.")
        if tutorial:
            print("(Tutorial: Mais de 21 = derrota. Cuidado na próxima!)")
    elif calcula_pontos(cartas_computador) > 21:
        print("O computador estourou! Você ganhou, show de bola!")
        if tutorial:
            print("(Tutorial: Computador passou de 21, então você leva essa!)")
    elif calcula_pontos(suas_cartas) > calcula_pontos(cartas_computador) and calcula_pontos(suas_cartas) <= 21:
        print("Você venceu, mandou muito bem!")
        if tutorial:
            print("(Tutorial: Seus pontos são maiores e não estourou. Vitória sua!)")
    elif calcula_pontos(suas_cartas) == calcula_pontos(cartas_computador):
        print("Empate! Foi por pouco, hein!")
        if tutorial:
            print("(Tutorial: Mesmos pontos? Empate! Ninguém ganha, ninguém perde.)")
    else:
        print("Que triste, você perdeu! O computador levou essa.")
        if tutorial:
            print("(Tutorial: Computador teve mais pontos sem estourar. Ele venceu dessa vez.)")

comeca_jogo()

while True:
    jogar_novamente = input("Quer jogar de novo? 's' pra sim, 'n' pra não: ").lower()
    if jogar_novamente not in ["s", "n"]:
        print("Calma aí, é só 's' ou 'n'! Tenta outra vez!")
        continue
    if jogar_novamente == "s":
        print("\n" * 20)  # Limpa a tela pra próxima rodada
        print(logo)
        suas_cartas = []
        cartas_computador = []
        comeca_jogo()
    else:
        print("Tchau, até a próxima aventura nas cartas!")
        input("Pressione Enter pra sair do rolê.")
        break