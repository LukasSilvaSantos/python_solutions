import random
import time
print(' Faça o seu cadastro para o sorteio. \n A cada R$10 doado, seu nome entrará na lista!')
doador1 = input('Qual seu nome: ')
valorDoado1 = float(input('Quanto você quer doar?: '))
if valorDoado1 >= 10:
    print(f'{doador1} doou R${valorDoado1}, seu nome vai entrar na lista do serteio!')
else:
    print(f'{doador1} só doou R${valorDoado1}, seu nome não vai entrar na lista do sorteio!')
doador2 = input('Qual seu nome: ')
valorDoado2 = float(input('Quanto você quer doar?: '))
if valorDoado2 >= 10:
    print(f'{doador2} doou R${valorDoado2}, seu nome vai entrar na lista do serteio!')
else:
    print(f'{doador2} só doou R${valorDoado2}, seu nome não vai entrar na lista do sorteio!')
doador3 = input('Qual seu nome: ')
valorDoado3 = float(input('Quanto você quer doar?: '))
if valorDoado3 >= 10:
    print(f'{doador3} doou R${valorDoado3}, seu nome vai entrar na lista do serteio!')
else:
    print(f'{doador3} só doou R${valorDoado3}, seu nome não vai entrar na lista do sorteio!')
listaSorteio = [doador1, doador2, doador3]
listaEnbaralhada = random.shuffle(listaSorteio)
listaVencedor = random.choice(listaSorteio)
print(f'lista do sorteio = {listaSorteio} \n Processando o vencedor...')
time.sleep(2)
print(f'O vencedor é: {listaVencedor}')
