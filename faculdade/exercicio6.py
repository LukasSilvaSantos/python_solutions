consumokWh = float(input('Qual foi a quantidade de KWh consumida?: '))
print('Qual foi o tipo de instalação? \n escreva: \n R para residência. \n I para indústria. \n C para comercio.')
instalacao = input('qual foi o tipo da instalação?: ')
if (instalacao == 'R'):
    if consumokWh <= 500:
        valor = 0.40
        print(f'O valor a ser pago é {valor:.2f} centavos!')
    else:
        valor = 0.65
        print(f'O valor a ser pago é {valor:.2f} centavos!')
elif instalacao == 'I':
    if consumokWh <= 1000:
        valor = 0.55
        print(f'O valor a ser pago é {valor:.2f} centavos!')
    else:
        valor = 0.60
        print(f'O valor a ser pago é {valor:.2f} centavos!')
elif instalacao == 'C':
    if consumokWh <= 5000:
        valor = 0.55
        print(f'O valor a ser pago é {valor:.2f} centavos!')
    else:
        valor = 0.60
        print(f'O valor a ser pago é {valor:.2f} centavos!')
input()
    

