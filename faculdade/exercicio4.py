print('digite os valores dos tres lados do triangulo!')
lado1 = int(input('digite o valor do primeiro lado: '))
lado2 = int(input('digite o valor do segundo lado: '))
lado3 = int(input('digite o valor do terceiro lado: '))
if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if (lado1 != lado2) and (lado2 != lado3) and (lado3 != lado1):
            print ('esse triangulo é um escaleno')
        else:
            if (lado1 == lado2)  and (lado2 == lado3):
                print ('esse triangulo é equilatero')
            else:
               print ('esse triangulo é isoceles')
    else:
        print('um dos valores escolhidos, não serve para formar um triangulo!')
else:
    print('um dos valores escolhidos, não serve para formar um triangulo!')
