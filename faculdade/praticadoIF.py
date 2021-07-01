# exercicio do par ou impar 
numero = int(input('digite um número inteiro: '))
divisão = numero % 2
if (divisão == 0):
    print('O número que você digitou é par!')
else:
    print('O número que você digitou é impar!')