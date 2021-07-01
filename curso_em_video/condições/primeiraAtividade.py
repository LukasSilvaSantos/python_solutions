nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) /2
print(f'Sua media foi {media:.1f}')
if media >= 6.0:
    print('sua media foi boa!, PARABÉNS!!.')
else:
    print('sua media foi ruim!, ESTUDE MAIS!!.')