valor1 = int(input('digite um valor: '))
if valor1 >= 100:
    cedulas100 = valor1 // 100
    valor1 = valor1 - cedulas100 * 100
if valor1 >= 50:
    cedula_50 = valor1 // 50
    valor1 = valor1 - cedula_50 * 50
if valor1 >= 20:
    cedula_20 = valor1 // 20
    valor1 = valor1 - cedula_20 * 20
if valor1 >= 10:
    cedula_10 = valor1 // 10
    valor1 = valor1 - cedula_10 * 10
if valor1 >= 5:
    cedula_5 = valor1 // 5
    valor1 = valor1 - cedula_5 * 5
if valor1:
    print(f'{valor1} notas de 1 real')