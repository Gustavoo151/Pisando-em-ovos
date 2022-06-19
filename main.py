from funcoes import movi_posi, verif_e_poke

print('Entrando')
movi_posi.posicao_atual()

while True:
    opcao_menu = verif_e_poke.menu_validado()

    match opcao_menu:
        case 9:
            movi_posi.posicao_atual()
            opcao_menu = verif_e_poke.menu_validado()

        case 8:
            movi_posi.go_up()
            movi_posi.posicao_atual()

        case 2:
            movi_posi.go_down()
            movi_posi.posicao_atual()

        case 4:
            movi_posi.go_left()
            movi_posi.posicao_atual()

        case 6:
            movi_posi.go_right()
            movi_posi.posicao_atual()

        case 5:
            verif_e_poke.pokedex()
            movi_posi.posicao_atual()

        case 0:
            print('Fim de jogo')
            break

    # if posicao_jog[1][5] or posicao_jog[1][6]:
    #   false

#Ainda Fal
#0 - Sair do Jogo [1, 5 ou 6]
# Dizer que tem um pokemon e perguntar se que substituir