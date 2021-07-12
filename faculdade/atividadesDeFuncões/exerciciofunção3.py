def ordem_crecente (a, b, c):
    if a < b and b < c:
        print(f'A ordem crescente é {a:.0f} {b:.0f} {c:.0f}',end=' ')
    elif b < c and c < a:
        print(f' A ordem crescente é {b:.0f} {c:.0f} {a:.0f}',end=' ')
    elif c < a and a < b:
        print(f' A ordem crescente é {c:.0f} {a:.0f} {b:.0f}',end=' ')
    elif c < b and b < a:
        print(f' A ordem crescente é {c:.0f} {b:.0f} {a:.0f}',end=' ')
    elif b < a and a < c:
        print(f' A ordem crescente é {b:.0f} {a:.0f} {c:.0f}',end=' ')
valor1 = float(input('digite um valor: '))
valor2 = float(input('digite um valor: '))
valor3 = float(input('digite um valor: '))
ordem_crecente(valor1, valor2, valor3)