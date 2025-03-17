import random

# Gerar número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Inicializar variáveis
tentativas = 0
max_tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

# Loop do jogo
while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Boaa Você acertou em {tentativas} tentativa(s).")
        break
    elif palpite < numero_secreto:
        print("baixo demais! Tente novamente.")
    else:
        print("altissimo! Tente novamente.")

# Encerramento do jogo
if palpite != numero_secreto:
    print(f"Fim do jogo! O número era {numero_secreto}.")