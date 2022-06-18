from funcoes import menu_validado, posicao_atual, go_up, go_down, go_left, go_right,pokedex, chance_capture, creat_pokemon, erase_resist

print('Entrando')
posicao_atual()

while True:
    opcao_menu = menu_validado()

    match opcao_menu:
        case 9:
            posicao_atual()
            opcao_menu = menu_validado()

        case 8:
            go_up()
            posicao_atual()

        case 2:
            go_down()
            posicao_atual()

        case 4:
            go_left()
            posicao_atual()

        case 6:
            go_right()
            posicao_atual()

        case 5:
            pokedex()
            posicao_atual()

        case 0:
            print('Fim de jogo')
            break

    # if posicao_jog[1][5] or posicao_jog[1][6]:
    #   false

#Ainda Fal
#0 - Sair do Jogo [1, 5 ou 6]
# Dizer que tem um pokemon e perguntar se que substituir