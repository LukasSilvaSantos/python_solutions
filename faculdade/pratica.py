nota1 = float(input('Qual foi a sua nota na primeira materia?: '))
nota2 = float(input('Qual foi a sua nota na segunda materia?: '))
nota3 = float(input('Qual foi a sua nota na terceira materia?: '))
if (nota1 >= 7 and nota2 >= 7 and nota3 >= 7):
    print('Parabéns, você passou em todas as materias!')
else:
    print('Você não foi reprovado!')
