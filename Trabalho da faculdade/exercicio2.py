def gerarEmail(nome, sobrenome, ru):
    inicial1 = nome[0]
    provedor = '@algoritmos.com.br'
    return(f'Sr {nome} {sobrenome}, seu email é: {inicial1}{sobrenome}'+ ru + provedor)
nome = input('digite seu primeiro nome: ')
sobrenome = input('digite seu sobrenome: ')
ru = input('digite os dois ultimos números do seu RU: ')
email = gerarEmail(nome, sobrenome, ru)
print(f'{email}')