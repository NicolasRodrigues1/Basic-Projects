import random 

def escolher_palavra():
    palavras = ['python', 'java', 'ruby', 'javascript', 'php']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra().lower()
    letras_erradas = []
    letras_corretas = []
    tentativas = 10
    
    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra secreta!")
    
    while True:
        palavra_misteriosa = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_misteriosa += letra + " "
            else:
                palavra_misteriosa += "_ "
                
        print(palavra_misteriosa)
        
        if palavra_misteriosa.replace(" ", "") == palavra:
            print(f"Parabéns! Você acertou a palavra secreta! {palavra}")
            break
        
        if len(letras_erradas) > 0:
            print("Letras erradas:", ", ".join(letras_erradas))
        
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra, tente outra.")
        elif letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print(f"Letra errada, você ainda tem {tentativas} tentativas.")
        
        if tentativas == 0:
            print(f"Suas tentativas acabaram! A palavra secreta era {palavra}")
            break
        
    jogar_novamente = input("Você deseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == "s":
        jogar_forca()
    else:
        print("Fim do jogo!")
        
jogar_forca()
