a = input().split(' ')
area_triangulo = float(a[0])*float(a[2])/2
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {float(a[2])**2*3.14159:.3f}')
print(f'TRAPEZIO: {(float(a[0])+float(a[1]))*float(a[2])/2:.3f}')
print(f'QUADRADO: {float(a[1])**2:.3f}')
print(f'RETANGULO: {float(a[0]) * float(a[1]):.3f}')
