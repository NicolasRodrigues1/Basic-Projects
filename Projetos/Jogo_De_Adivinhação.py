import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    print("Bem-Vindo ao jogo de adivinhação!")
    print("Você tem 10 tentativas para conseguir descobrir o número secreto.")
    print(" ")
    
    while tentativas < max_tentativas: 
        tentativa = int(input("Digite um número: "))
        tentativas += 1
        
        if tentativa < numero_secreto:
            print("Tente colocar um número maior!")
        elif tentativa > numero_secreto:
            print("Tente colocar um número menor!")
        else:
            print(f"Parabéns! Você adivinhou o número secreto em {tentativas} tentativas!")
            print(f"O número secreto era {numero_secreto}")
            break

        if tentativas == max_tentativas:
            print("Você não conseguiu adivinhar o número secreto.")
  
jogo_adivinhacao()
