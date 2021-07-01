       #selecionando um item na lista.
       
#usamos a biblioteca random para escolher de forma aleatoria qual aluno seria escolhido
#a função da biblioteca random que foi usada é a função choice que pode ser puxada com from import random choice.
#tambem usamos a função lista ultilizando os [] para que o computador identifique que se trata de uma lista.

import random
aluno1 = str(input(' Qual o nome do primeiro aluno?: '))
aluno2 = str(input(' Qual o nome do segundo aluno?: '))
aluno3 = str(input(' Qual o nome do terceiro aluno?: '))
aluno4 = str(input(' Qual o nome do quarto aluno?: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print(f' O aluno escolhido foi {escolhido}.')

#segunda forma de resolver com o codigo mais simplificado.

import random 
alunos = input('Nome do primeiro aluno: '), input('nome do segundo aluno: '), input('nome do terceiro aluno: ')
resultado = random.choice(alunos)
print(f'O aluno escolhido foi {resultado}')