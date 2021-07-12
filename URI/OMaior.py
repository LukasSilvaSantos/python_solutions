numeros = input().split(' ')
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])
maiorab = (a + b + abs(a-b))/2
maiorabc = (maiorab + c + abs(maiorab-c))/2
print(f'{(maiorabc):.0f} eh o maior')
