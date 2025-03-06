import random

def cara_coroa():
    moeda = random.randint(1, 10)
    print('Bem-vindo ao jogo de Cara ou Coroa!')
    jogada = (input('Vou jogar a moeda. Pressione "c" para cara ou "r" para coroa: ')).lower()
    print('A moeda está sendo jogada...')
    print('A moeda caiu em:', moeda)
    if moeda % 2 == 0:
        if jogada == 'c':
            print('Sim, você ganhou! A moeda caiu em Cara.')
        else:
            print('Desculpe, você perdeu! A moeda caiu em Cara.')
    else:
        if jogada == 'r':
            print('Sim, você ganhou! A moeda caiu em Coroa.')
        else:
            print('Desculpe, você perdeu! A moeda caiu em Coroa.')

while True:
    cara_coroa()
    novamente = input('Quer jogar novamente? (s/n): ').lower()
    if novamente != 's':
        break

print('Obrigado por jogar!')
print("Pressione Enter para sair")         
