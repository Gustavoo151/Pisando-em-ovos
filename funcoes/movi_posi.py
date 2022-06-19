# Funções de posição e movimentação
from funcoes import verif_e_poke

mapa = [["A","A","A","A","A", "" ,"" ,"A","A","A","A","A"],
        ["A","","","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"A","" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","E","A","E","E","E","G","G","G","A"],
        ["A","" ,"" ,"" ,"A","G","G","G","G","G","G","A"],
        ["A","E","E","E","A","G","G","G","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"G","G","G","A"],
        ["A","A","E","E","E","A","A","A","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","" ,"E","E","" ,"E","E","E","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" , "A"],
        ["A","A","A","A","A","A","G","G","G","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"G","G","G","" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","" ,"" ,"E","E","E","E","E","E","A"],
        ["A","" ,"G","G","G","G","" ,"" ,"G","G","G","A"],
        ["A","G","G","G","" ,"" ,"" ,"G","G","" ,"" ,"A"],
        ["A","A","A","A","A","A","G","A","A","A","A","A"]]

posicao_jog = [19, 6]


def mapa_localizacao(): # Localização do jogador no mapa
    return mapa[posicao_jog[0]][posicao_jog[1]]


def posicao_atual(): # Mostrar posição do jogador  
    print(f'Posição atual do jogador: Linha: {posicao_jog[0]} , Coluna: {posicao_jog[1]}')


def go_up(): # Movimentação para cima
    posicao_jog[0] -= 1
    if mapa_localizacao() == 'A' or mapa_localizacao() == 'E':
        posicao_jog[0] += 1
        print('Bump!')
    else:
        verif_e_poke.chance_capture()


def go_down(): # Movimentação para baixo
    if posicao_jog[0] < 19 and mapa_localizacao() != 'A':
        posicao_jog[0] += 1
        verif_e_poke.chance_capture()
    else:
        print('Bump!')


def go_left(): # Movimentação para esquerda
    if posicao_jog[1] > 0:
        posicao_jog[1] -= 1
        if mapa_localizacao() == 'A' or mapa_localizacao() == 'E':
            posicao_jog[1] += 1
            print('Bump!')
        else:
            verif_e_poke.chance_capture()


def go_right(): # Movimentação para direita
    if posicao_jog[1] <= 12:
        posicao_jog[1] += 1
        if mapa_localizacao() == 'A' or mapa_localizacao() == 'E':
            posicao_jog[1] -= 1
            print('Bump!')
        else:
            verif_e_poke.chance_capture()
