valor1 = float(input('qual o valor inicial?: '))
valor2 = float(input('qual o valor final?: '))
valor = valor1
while (valor1 <= valor2):
    if (valor1 % 2) == 0:
        print(f'{valor1}')
    valor1 = valor1 + 1

