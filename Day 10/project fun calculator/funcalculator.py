import random

def calculadora():
    print("Calculadora Divertida!")
    print("Operações: +, -, *, /")
    
    # Lista de comentários engraçados com tom de piada
    comentarios = [
        "Você deve tudo isso??? Tá devendo até pro cálculo!",
        "Até minha avó calcula mais rápido que isso!",
        "Números tão fáceis e você ainda usa calculadora?",
        "Parabéns, você não explodiu a matemática... ainda!",
        "Isso aí é resultado ou chute de loteria?",
        "O número agradece por não ter errado feio!",
        "Tá vendo? Não é tão difícil assim, né?",
        "Cê jura que precisava de ajuda pra isso?",
        "Olha, o gênio da lâmpada dos números!",
        "Deu certo? Milagre ou sorte?",
        "Esse cálculo tá mais perdido que você na escola!",
        "A calculadora chorou pra te ajudar nisso!",
        "Nem o Google faz tão devagar, hein!",
        "Você e os números: uma comédia sem fim!",
        "A matemática tá rindo da sua cara agora!",
        "Esse resultado tá mais ou menos... mais pra menos!",
        "Eu que fiz o trabalho pesado aqui, admite!",
        "Você + números = confusão garantida!",
        "Tá orgulhoso? Minha planta calcula melhor!",
        "Se fosse prova, já era, hein!"
    ]
    
    while True:
        try:
            # Obter primeiro número
            num1 = float(input("Digite o primeiro número: "))
            
            # Obter operação
            operacao = input("Digite a operação (+, -, *, /): ")
            
            # Obter segundo número
            num2 = float(input("Digite o segundo número: "))
            
            # Realizar cálculo baseado na operação
            if operacao == '+':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
                
            elif operacao == '-':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
                
            elif operacao == '*':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
                
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Não dá pra dividir por zero, né?")
                else:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")
            
            else:
                print("Operação inválida! Use +, -, *, ou /")
                continue
            
            # Exibir um comentário engraçado aleatório
            comentario = random.choice(comentarios)
            print(f"😂 {comentario}")
            
            # Perguntar se quer continuar
            novamente = input("Calcular de novo? (sim/não): ").lower()
            if novamente != 'sim':
                print("Valeu por usar a Calculadora Divertida!")
                break
                
        except ValueError:
            print("Erro: Digite números válidos, por favor!")
            
        except Exception as e:
            print(f"Deu um erro: {e}")

# Rodar a calculadora
if __name__ == "__main__":
    calculadora()