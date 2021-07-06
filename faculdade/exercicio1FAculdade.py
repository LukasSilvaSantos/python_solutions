print(' vamos calcular o desconto nos produtos. \n digite na tela o valor do produto é o valor do desconto. \n OBS: (Não coloque nenhum caracter no valor do produto ou do desconto, só coloque os números.)')
preçodoProduto = input('qual o preço do produto?: ')
desconto = input('qual o valor do desconto?: ')
if (preçodoProduto.isnumeric() and desconto.isnumeric() == True):
    porcentagem = float(preçodoProduto) * float(desconto) / 100
    valorFinal = float(preçodoProduto) - porcentagem
    print(f'o valor do produto com o desconto aplicado será de R${valorFinal:.2f}')

    