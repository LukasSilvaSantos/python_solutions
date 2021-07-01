#Crie um programa que leia o nome completo de uma pessoa e mostre:
  #O nome com todas as letras maiúsculas.
  #O nome com todas as letras minúsculas.
  #Quantas letras ao todo (sem considerar os espaços.)
  #Quantas letras tem o primeiro nome.
MeuNome = str(input(' digite seu nome!: ')).strip()
print(f' Analisando seu nome...\n O seu nome é {MeuNome}.\n Todo em maiúsculo é {MeuNome.upper()}.\n Todo em minúsculo é {MeuNome.lower()}.\n O seu nome tem {len(MeuNome) - MeuNome.count(" ")} ')
print(f' Seu primeiro nome tem {MeuNome.find(" ")} letras.')
