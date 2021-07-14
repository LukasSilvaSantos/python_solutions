import random
print('olá, eu sou um bot MUITO LEGAL!, vamos brincar de pedra, papel ou tesoura?')
while True:
    sim_ou_nao = input('sim ou não?: ')
    if (sim_ou_nao != 'sim' and sim_ou_nao != 'não'):
        print('ALAN MALDITO!, não tente me bugar, você não vai conseguir! HAHAHAHA \n TENTE OUTRA VEZ!')
        continue
    elif (sim_ou_nao == 'não'):
        print('ok, você não quer brincar..., xau!')
        break
    if (sim_ou_nao == 'sim'):
        print('OK, vamos começar!')
    escolha_usuario = input('o que você escolhe?: ')
    if (escolha_usuario == 'pedra' or escolha_usuario == 'papel' or escolha_usuario == 'tesoura'):
        lista = ['pedra', 'papel', 'tesoura']   
        escolha_maquina = random.choice(lista)
        if escolha_maquina == escolha_usuario:
            print(f'maquina escolheu {escolha_maquina}')
            print('EMPATE!')
        elif escolha_maquina == 'pedra' and escolha_usuario == 'papel':
            print(f'maquina escolheu {escolha_maquina}')
            print('maquina perdeu!')
        elif escolha_maquina == 'pedra' and escolha_usuario == 'tesoura':
            print(f'maquina escolheu {escolha_maquina}')
            print('maquina ganhou!')
        elif escolha_maquina == 'papel' and escolha_usuario == 'tesoura':
            print(f'maquina escolheu {escolha_maquina}')
            print('maquina perdeu!')
        elif escolha_maquina == 'papel' and escolha_usuario == 'pedra':
            print(f'maquina escolheu {escolha_maquina}')
            print('maquina ganhou!')
        elif escolha_maquina == 'tesoura' and escolha_usuario == 'pedra':
            print(f'maquina escolheu {escolha_maquina}')
            print('maquina perdeu!')
        elif escolha_maquina == 'tesoura' and escolha_usuario == 'papel':
            print(f'maquina escolheu {escolha_maquina}')
            print('maquina ganhou!')
    else:
        print(' ALAN MALDITO!, não tente me bugar, você não vai conseguir! HAHAHAHA \n TENTE OUTRA VEZ!')
print('Encerrando o programa...')
input()
        