# Projeto 1 - Desenvolvimento de Game Python

# Import 
import random
from os import system, name

# Função para limpar tela
def limpa_tela():

    # Windows
    if name  == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras
    palavras = ['banana','abacate','uva','morango','laranja']

    # Escolhe a palavra aleatória
    palavra = random.choice(palavras)

    # List comprehenssion
    letras_descobertas = ['_' for letra in palavra]

    # Nímero de chances
    chances = 10

    # Lista para letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior que zero
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativas
        tentativa = input("\nDigite uma letra: ").lower()

        if (tentativa in palavra):
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break
        
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação!\n")





