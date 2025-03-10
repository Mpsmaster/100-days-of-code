def vida_em_semanas():
    print("Bem-vindo ao Calculador de Vida em Semanas, o terror dos ansiosos!")

    while True:
        escolha_vida_restante = input("Quer saber quantas semanas ou dias te restam nessa aventura chamada vida? Digite 's' pra semanas ou 'd' pra dias: ")
        if escolha_vida_restante in ["s", "d"]:
            if escolha_vida_restante == "s":
                
                while True:
                    try:
                        idade = int(input("Quantos anos você já aguentou nesse planeta? \n"))
                        if idade > 90:
                            print("Caramba, você é praticamente um dinossauro! Já passou da média da humanidade!")
                            continue
                        elif idade < 0:
                            print("Oi? Você ainda tá no ventre ou é viajante do tempo?")
                            continue
                        elif idade == 90:
                            print("Parabéns, você chegou na linha de chegada da média humana! Tá na prorrogação!")
                            continue
                        elif idade == 0:
                            print("Recém-saído do forno, hein? Aproveita o cheirinho de bebê!")
                            continue
                        else:
                            anos_restantes = 90 - idade
                            semanas_restantes = anos_restantes * 52
                            print(f"Olha só: te sobram {semanas_restantes} semanas pra fazer algo útil... ou só comer brigadeiro!")
                    except ValueError:
                        print("Ei, coloca um número decente aí, não inventa moda!")
                        continue
                    break
            else:
                while True:
                    try:
                        idade = int(input("Quantos anos você já aguentou nesse planeta? \n"))
                        if idade > 90:
                            print("Caramba, você é praticamente um dinossauro! Já passou da média da humanidade!")
                            continue
                        elif idade < 0:
                            print("Oi? Você ainda tá no ventre ou é viajante do tempo?")
                            continue
                        elif idade == 90:
                            print("Parabéns, você chegou na linha de chegada da média humana! Tá na prorrogação!")
                            continue
                        elif idade == 0:
                            print("Recém-saído do forno, hein? Aproveita o cheirinho de bebê!")
                            continue
                        else:
                            anos_restantes = 90 - idade
                            dias_restantes = anos_restantes * 365
                            print(f"Olha o drama: te sobram {dias_restantes} dias pra gastar com Netflix ou tentar ser fitness!")
                    except ValueError:
                        print("Ei, coloca um número decente aí, não inventa moda!")
                        continue
                    break
        else:
            print("Ô, meu filho, é 's' ou 'd', não é prova de criatividade!")
            continue
        break

vida_em_semanas()
while True:
    perguntar_de_novo = input("Quer calcular de novo e ficar mais deprimido? Digite 'sim' ou 'não': ")
    if perguntar_de_novo in ["sim", "não"]:
        if perguntar_de_novo == "sim":
            vida_em_semanas()
        else:
            print("Tchau, até a próxima crise existencial!")
            input("Aperta Enter pra fugir dessa realidade.")
            break
    else:
        print("É 'sim' ou 'não', não enrola que eu não sou terapeuta!")
        continue