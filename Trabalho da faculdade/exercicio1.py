nome_aluno = input('Qual o nome do aluno?: ')
conceito1 = 'E'
conceito2 = 'D'
conceito3 = 'C'
conceito4 = 'B'
conceito5 = 'A'
while nome_aluno != 'sair':
    nota_final = float(input('Qual a sua nota final?: '))
    if nota_final <= 2.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito {conceito1}')
    elif nota_final <= 4.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito {conceito2}')
    elif nota_final <= 6.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito {conceito3}')
    elif nota_final <= 8.9:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito {conceito4}')
    elif nota_final <= 10:
        print(f' O aluno {nome_aluno} tirou nota {nota_final} e se enquadra no conceito {conceito5}')
    print('Para encerrar o programa, digite: sair.')
    nome_aluno = input('Qual o nome do aluno?: ')
print('Encerrando o programa...')
