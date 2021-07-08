# Eu começo o código pedindo o nome do aluno.
nome_aluno = input('Qual o nome do aluno?: ')
# Depois eu faço um laço de repetição, com a seguinte condição: se o nome do aluno for diferente de sair, execute o que está sendo pedido a baixo. 
while nome_aluno != 'sair':
    nota_final = float(input('Qual a sua nota final?: '))
# Para dar o resultado da saída pedido no enunciado da questão, utilizei as funções de condição, seguindo o conceito apresentado na tabela, Exemplo em pseudocódigo: se, nota do aluno for menor ou igual a 2.9: mostrar na tela(O aluno Fabio José tirou nota 2.5 e se enquadra no conceito E.)
    if nota_final <= 2.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito E')
    elif nota_final <= 4.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito D')
    elif nota_final <= 6.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito C')
    elif nota_final <= 8.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito B')
    elif nota_final <= 10:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito A')
    # E por fim, eu coloquei como critério para o encerramento do programa, digitar a palavra “sair”.
    print('Para encerrar o programa, digite: sair.')
    nome_aluno = input('Qual o nome do aluno?: ')
print('Encerrando o programa...')
