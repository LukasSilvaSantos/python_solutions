print('CAlCULANDO... \n + = ADIÇÃO \n - = Subtração \n * = Multiplicação \n / = Divisão.')
operação = input('qual operação deseja fazer?: ')
numero1 = float(input('digite um valor: '))
numero2 = float(input('digite um valor: '))
while (operação != 'sair'):
    if (operação == '+'):
        soma = numero1 + numero2
        print(f'A soma de {numero1} + {numero2} é {soma}.')
    elif (operação == '-'):
        soma = numero1 - numero2
        print(f'A subtração de {numero1} - {numero2} é {soma}.')
    elif (operação == '*'):
        soma = numero1 * numero2
        print(f'A multiplicação de {numero1} * {numero2} é {soma}.')
    elif (operação == '/'):
        soma = numero1 / numero2
        print(f'A divisão de {numero1} / {numero2} é {soma}.')
    print('CAlCULANDO... \n + = ADIÇÃO \n - = Subtração \n * = Multiplicação \n / = Divisão.')
    operação = input('qual operação deseja fazer?: ')
    numero1 = float(input('digite um valor: '))
    numero2 = float(input('digite um valor: '))
print('Encerrando o programa...')
