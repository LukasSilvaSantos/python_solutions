def borda(s1):
    tamanho = len(s1)
    if tamanho:
        print('+','-' * tamanho,'+')
        print('|',s1,'|')
        print('+','-' * tamanho,'+')
borda('lucas insano')