import random
import time

print("Bem-vindo ao Jogo Testador de Sorte! Aqui você só perde se não ganhar!")
print("A gente escolhe um número mágico, e se pelo menos dois dos quatro números forem divisíveis por ele, você ganha fácil!")
input("Aperte Enter para começar!")
vitorias = 0

while True:
    num_div = random.randint(2, 4)
    print(f"\nGira aí! Se dois números forem divisíveis por {num_div}, a festa é sua!")
    
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)
    num4 = random.randint(1, 20)
    
    print("Girando os tambores...")
    time.sleep(1)
    print(f"Primeiro número: {num1}")
    time.sleep(1)
    print(f"Segundo número: {num2}")
    time.sleep(1)
    print(f"Terceiro número: {num3}")
    time.sleep(1)
    print(f"Quarto número: {num4}")
    
    contagem = 0
    if num1 % num_div == 0:
        contagem += 1
    if num2 % num_div == 0:
        contagem += 1
    if num3 % num_div == 0:
        contagem += 1
    if num4 % num_div == 0:
        contagem += 1
    
    if contagem >= 2:
        print("É isso aí! Você ganhou de novo, seu sortudo!")
        vitorias += 1
        print(f"Vitórias acumuladas: {vitorias}")
    else:
        print("Nossa, perdeu? Que azar raro hein!")
    
    jogar_novamente = input("Quer mais uma vitória fácil? (sim/não) ").lower()
    if jogar_novamente in ["não", "n"]:
        break

print(f"\nValeu, lenda! Você terminou com {vitorias} vitórias no bolso!")