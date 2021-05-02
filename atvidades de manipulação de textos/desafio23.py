numero = int(input('digite um numero de no maximo 4 digitos: '))
U = numero // 1 % 10
D = numero // 10 % 10
C = numero // 100 % 10 
M = numero // 1000 % 10
print(f'Analisando o número {numero}...\n Unidade: {U}\n Dezena: {D}\n Centena: {C}\n Milhar: {M}')