dias = float(input('quantos dias o carro foi alugado?: '))
km = float(input('quantos km foram percorridos?: '))
pago = km*0.15+dias*60
print(f'o valor a ser pago é {pago:.2f}!')