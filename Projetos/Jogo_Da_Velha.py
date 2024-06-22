def imprimir_tabuleiro(tabuleiro):
    print(' ' + tabuleiro[0] + ' | ' + tabuleiro[1] + ' | ' + tabuleiro[2])
    print('-----------')
    print(' ' + tabuleiro[3] + ' | ' + tabuleiro[4] + ' | ' + tabuleiro[5])
    print('-----------')
    print(' ' + tabuleiro[6] + ' | ' + tabuleiro[7] + ' | ' + tabuleiro[8])
    
def verificar_vitoria(tabuleiro, jogador):
        return ((tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or
                (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or
                (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) or
                (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or
                (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or
                (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or
                (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or
                (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador))
        
def jogar_jogo_da_velha():
        tabuleiro = [' '] * 9
        jogador_atual = 'X'
        jogo_ativo = True
        
        print("Bem-Vindo ao jogo da Velha!")
        
        while jogo_ativo:
            imprimir_tabuleiro(tabuleiro)
            posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            
            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador_atual
                if verificar_vitoria(tabuleiro, jogador_atual):
                    imprimir_tabuleiro(tabuleiro)
                    print("Parabéns! Jogador {jogador_atual} ganhou!")
                    jogo_ativo = False
                elif ' ' not in tabuleiro:
                    imprimir_tabuleiro(tabuleiro)
                    print("Empate!")
                    jogo_ativo = False
                else:
                    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
            else:
                print("Posição já ocupada, escolha outra posição para poder jogar.")
                
        novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if novamente == 's':
            jogar_jogo_da_velha()
        else:
            print("Obrigado por jogar!")
            
jogar_jogo_da_velha()
