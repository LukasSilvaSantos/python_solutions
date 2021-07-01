print('Escolha qual fruta você vai querer comprar!')
print('1 para maçã')
print('2 para banana')
print('3 para laranja')
produto = int(input('qual fruta você vai escolher?: '))
quantidade = int(input('quantas você vai comprar?: '))
if (produto == 1):
    pagar = quantidade * 2.30
    print(f'você comprou {quantidade} maçãs e o valor é {pagar}')
else:
    if (produto == 2):
        pagar = quantidade * 1.85
        print(f'você comprou {quantidade} bananas e o valor a ser pago é {pagar}')
    else:
        if (produto == 3):
            pagar = quantidade * 3.60
            print(f'você comprou {quantidade} laranjas e o valor a pagar é {pagar}')
