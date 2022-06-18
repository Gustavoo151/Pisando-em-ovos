from random import randint
import re

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

menu = ('''
    Bem-vindo!
A qualquer momento você pode escolher uma das opções:
9 - Para abrir esse menu
8 - Subir
2 - Descer
4 - Ir para esquerda
6 - Ir para direta
5 - Abrir Pokedex
0 - Sair do Jogo''')


def posicao_joga():
    posicao_jog = [19, 6]
    return posicao_jog


especie_pokemon = ['Ratata', 'Pidgey', 'Weedle', 'Caterpie', 'Paras', 'Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu', 'Evee']

dados_pokemon = {'Nome':'None', 'HP':0, 'Atk':0, 'Def':0, 'Speed':0}


def mapa_localizacao(): # Localização do jogador no mapa
    return mapa[posicao_joga()[0]][posicao_joga()[1]]


def menu_validado(): #Validação Menu
    print(menu)
    opcao = input()
    while not opcao.isnumeric() or int(opcao) not in [9, 8, 2, 4, 6, 5, 0]:
        print('Opção inválida!')
        opcao = input()
    return int(opcao)


def posicao_atual(): # Mostrar posição do jogador  
    print(f'Posição atual do jogador: Linha: {posicao_joga()[0]} , Coluna: {posicao_joga()[1]}')


def erase_resist(): # Zerar resitro
    dados_pokemon['Nome'] = 0
    dados_pokemon["HP"] = 0
    dados_pokemon["Atk"] = 0
    dados_pokemon['Def'] = 0
    dados_pokemon["Speed"] = 0
    dados_pokemon["Atk"] = 0


def creat_pokemon(): # Cria Pokemon
    dados_pokemon['Nome'] = especie_pokemon[randint(0,9)]
    dados_pokemon["HP"] = randint(0, 100)
    dados_pokemon["Atk"] = randint(0, 100)
    dados_pokemon['Def'] = randint(0, 100)
    dados_pokemon["Speed"] = randint(0, 100)
    dados_pokemon["Atk"] = randint(0, 100)


def chance_capture(): # Captura Pokemon
    chance = randint(1,2)
    if chance == 2:
        capture = input('Capturar ou correr? [1-Capturar ou 2-Correr] ')
        if int(capture) == 1:
            creat_pokemon()
            print('Pokemon capturado')
        else:
            print('Fujão')


def pokedex(): # Funções da Pokedex
    while True:    
        opcao = input('''
Digite:
1- Para Listar Detalhes
2- Para Apagar Registro
0- Para voltar ao menu principal
Escolha uma ação:
''')

        while not opcao.isnumeric() or int(opcao) not in [0, 1, 2]:
            opcao = input('Digite um opção válida: ')

        match int(opcao):
            case 0:
                break
            case 1:
                [print(f'{x}: {y}') for x,y in dados_pokemon.items()]
            case 2:
                erase_resist()
                print('Resistro apagado')


def go_up(): # Movimentação para cima
    posicao_joga()[0] -= 1
    if mapa_localizacao() == 'A' or mapa_localizacao() == 'E':
        posicao_joga()[0] += 1
        print('Bump!')
    else:
        chance_capture()


def go_down(): # Movimentação para baixo
    if posicao_joga()[0] < 19 and mapa_localizacao() != 'A':
        posicao_joga()[0] += 1
        chance_capture()
    else:
        print('Bump!')


def go_left(): # Movimentação para esquerda
    if posicao_joga()[1] > 0:
        posicao_joga()[1] -= 1
        if mapa_localizacao() == 'A' or mapa_localizacao() == 'E':
            posicao_joga()[1] += 1
            print('Bump!')
        else:
            chance_capture()


def go_right(): # Movimentação para direita
    if posicao_joga()[1] <= 12:
        posicao_joga()[1] += 1
        if mapa_localizacao() == 'A' or mapa_localizacao() == 'E':
            posicao_joga()[1] -= 1
            print('Bump!')
        else:
            chance_capture()



def testando():
    pocao_jog = [19, 6]
    return pocao_jog

testando()[0] += 13
print(testando())