numero1 = int(input('escreva um numero inteiro: '))
numero2 = int(input('escreva um numero inteiro: '))
operação = input('Escolha uma dessas operações: (+), (-), (*), (/): ')
if operação == '+':
    calculo = (numero1 + numero2)
    print (f'O resultado da operação foi {calculo}')
else:
    if operação == '-':
        calculo = (numero1 - numero2)
        print (f'O resultado da operação foi {calculo}')
    else:
        if operação == '*':
            calculo = (numero1 * numero2)
            print (f'O resultado da operação foi {calculo}')
        else:
            if operação == '/':
                calculo = (numero1 / numero2)
                print (f'O resultado da operação foi {calculo}')        