preçodoProduto = float(input('qual o preço do produto?: '))
desconto = float(input('qual o valor do desconto?: '))
porcentagem = preçodoProduto * (desconto / 100)
valorFinal = preçodoProduto - porcentagem
print(f'o valor do produto com o desconto aplicado será de R${valorFinal}.')