kmpercorrido = float(input('quantos KM voçê percorreu com o veículo?: '))
diaAlugado = int(input('Por quantos dias voçê alugou o carro?: '))
somadia = diaAlugado * 60
somakm = kmpercorrido * 0.15
resultado = somadia + somakm
print(f'Voçê alugou o carro por {diaAlugado} dias e percorreu {kmpercorrido} quilometros!, o valor total a ser pago é de R${resultado}!')
