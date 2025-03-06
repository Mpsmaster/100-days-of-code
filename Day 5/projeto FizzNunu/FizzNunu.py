import time  # Import the time module for timing

print("Bem vindo ao jogo do FizzNunu! As regras são simples:\n "
      "Conte de 1 a 100, mas com algumas diferenças:\n "
      "Se o número for divisível por 2, fale Fizz.\n "
      "Se o número for divisível por 3, fale Nunu.\n "
      "Se o número for divisível por ambos, fale FizzNunu.\n "
      "Caso contrário, fale apenas o número.\n "
      "Dispute com seus amigos e veja quem acerta mais em menos tempo!\n")

input("Press Enter to continue...")  # Pauses and waits for user to press Enter

# Record the start time
start_time = time.time()

# Game loop
for number in range(1, 101):
    if number % 2 == 0 and number % 3 == 0:
        print("FizzNunu")
    elif number % 3 == 0:
        print("Nunu")
    elif number % 2 == 0:
        print("Fizz")
    else:
        print(number)
    input("Press Enter to continue...")

# Record the end time
end_time = time.time()

# Calculate elapsed time in seconds
elapsed_time = end_time - start_time

# Display the total time taken
print(f"\nParabéns! Você completou o jogo em {elapsed_time:.2f} segundos!")