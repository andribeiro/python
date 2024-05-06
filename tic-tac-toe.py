from IPython.display import clear_output

def mostra_quadro(quadro):
    clear_output()
    print(quadro[7] + '|' + quadro[8] + '|' + quadro[9] + '         7|8|9')
    print(quadro[4] + '|' + quadro[5] + '|' + quadro[6] + '   ->>   4|5|6')
    print(quadro[1] + '|' + quadro[2] + '|' + quadro[3] + '         1|2|3')


def ler_numero():
    numero_lido = 0
    numero_valido = False
    
    while numero_valido == False or (numero_lido < 1 or numero_lido > 9):
        leu = input('Insere número pretendido de 1-9: ')
        
        numero_valido = leu.isnumeric()
        if numero_valido == True:
            numero_lido = int(leu)
        else:
            print('Número inválido, tenta de 1-9')
    
    return numero_lido


def insere_jogada(quadro, posicao, simbolo):
    
    if simbolo not in ('X','O'):
        print("Símbolo errado {} - Valores possíveis: X ou O".format(simbolo))
        return False
    
    if posicao < 1 or posicao > 9:
        print("Jogada fora do quadro {}. Posição tem de ser entre 1-9".format(posicao))
        return False
    
    if quadro[posicao] != ' ':
        print("Jogada errada: essa posição já está ocupada com {}".format(quadro[posicao]))
        return False
    
    quadro[posicao] = simbolo
    return True


def ver_se_ganhou(quadro, simbolo):
    
    if simbolo not in ('X','O'):
        print("Símbolo errado {} - Valores possíveis: X ou O".format(simbolo))
        return False
    
    ganhou = False
    ganhou = ganhou or (quadro[7] == quadro[8] == quadro[9] == simbolo) #linha topo
    ganhou = ganhou or (quadro[4] == quadro[5] == quadro[6] == simbolo) #linha meio
    ganhou = ganhou or (quadro[1] == quadro[2] == quadro[3] == simbolo) #linha baixo
                                     
    ganhou = ganhou or (quadro[7] == quadro[4] == quadro[1] == simbolo) #coluna esquerda
    ganhou = ganhou or (quadro[8] == quadro[5] == quadro[2] == simbolo) #coluna  meio
    ganhou = ganhou or (quadro[9] == quadro[6] == quadro[3] == simbolo) #coluna direita
                                     
    ganhou = ganhou or (quadro[7] == quadro[5] == quadro[3] == simbolo) #diagonal esq->dir
    ganhou = ganhou or (quadro[9] == quadro[5] == quadro[1] == simbolo) #diagonal dir->esq
    
    if ganhou == True:
        print('Parabéns {} ganhou o jogo do TIC-TAC-TOE !!!!'.format(jogadores[simbolo]))
        
    return ganhou


def ler_nome(simbolo):
    nome = input('Introduza o nome do Jogador {}: '.format(simbolo))
    
    if not nome.isalpha():
        print('Nome inválido')
        return ler_nome(simbolo)
    
    return nome


def ler_continuar():
    continuar = input('Jogar novamente? S ou N: ').upper()
    
    if continuar not in ('S','N'):
        print('Opção inválida')
        return ler_continuar()
    
    if 'S' == continuar:
        clear_output()
        return True
    
    return False


def quadro_cheio(quadro):
    for i in range(1,10):        
        if tem_espaco(quadro, i):
            return False

    return True


def tem_espaco(quadro, posicao):
    return quadro[posicao] == ' '


# MAIN
continuar_jogo = True

while continuar_jogo == True:
    clear_output()

    # QUADRO - Representação de teclado numérico (numpad)
    # 7|8|9
    # 4|5|6
    # 1|2|3
    quadro = [' '] * 10 # posição 0 vai ser ignorada e usamos indice de 1-9 respectivamente
    jogadores = {'X': '', 'O': ''}

    print('Bem vindos ao Tic-Tac-Toe do *** André Gaspar Ribeiro *** \n')
    
    jogadores['X'] = ler_nome('X')
    jogadores['O'] = ler_nome('O')

    mostra_quadro(quadro)
    ganhou = False
    num_jogada = 0
    
    while True:
        
        posicao_valida = False
        
        if num_jogada % 2 == 0:
            print('*** Jogador X [{}] ***'.format(jogadores['X']))
            joga_posicao = ler_numero()
            posicao_valida = insere_jogada(quadro, joga_posicao, 'X')
            mostra_quadro(quadro)
            ganhou = ver_se_ganhou(quadro, 'X')
        else:
            print('*** Jogador O [{}] ***'.format(jogadores['O']))
            joga_posicao = ler_numero()
            posicao_valida = insere_jogada(quadro, joga_posicao, 'O')
            mostra_quadro(quadro)
            ganhou = ver_se_ganhou(quadro, 'O')
        
        if ganhou == True:
            print('Fim do Jogo')
            break
            
        if quadro_cheio(quadro) == True:
            print('Empate! (*_*)')
            break

        if posicao_valida:
            num_jogada += 1

    continuar_jogo = ler_continuar()

