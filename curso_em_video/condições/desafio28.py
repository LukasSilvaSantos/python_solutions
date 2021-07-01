from random import randint
from time import sleep
NumeroDoPC = randint(0, 5)
print('Pensei em um número entre 0 e 5')
NúmeroDousuario = int(input('Tente adivinhar: '))
print('PROCESSANDO...')
sleep(3)
if (NúmeroDousuario  == NumeroDoPC):
    print('Parabéns voçê acertou!')
else:
    print('Que pena, voçê errou!.')
input()