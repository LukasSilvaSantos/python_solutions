VelocidadeDoCarro = float(input('Qual a valociade do carro?: '))
if (VelocidadeDoCarro > 80):
    print('MULTADO! Voçê excedeu o limite de velocidade, que é, 80km/h')
    multa = (VelocidadeDoCarro - 80) * 7
    print(f'Voçê devera pagar {multa:.2f} de multa!')
print('Tenha um bom dia! Dirija com segurança!')