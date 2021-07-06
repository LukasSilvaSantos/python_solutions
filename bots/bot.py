import random
print('olá, eu sou um bot MUITO LEGAL!, vamos brincar de pedra, papel ou tesoura?')
sim_ou_nao = input('sim ou não?: ')
if sim_ou_nao == 'sim':
    print('OK, vamos começar!')
else:
    print('ok, você não quer brincar..., xau!')
escolha_usuario = input('o que você escolhe?: ')
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
input()