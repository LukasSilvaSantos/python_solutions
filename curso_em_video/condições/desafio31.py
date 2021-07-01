distanciaDaViagem = float(input('Qual a distância da sua viagem?: '))
valorDaVG = distanciaDaViagem * 0.50
if (distanciaDaViagem >= 200):
    resultado = distanciaDaViagem * 0.45
    print(f'O valor da sua viagem com disconto vai ser R${resultado:.2f}')
else:
    print(f'O valor da sua viagem vai ser R${valorDaVG:.2f}')

