nome = input('qual o seu nome?: ')
idade = int(input('qual a sua idade?: '))
usuario = 'Vinicius'
if (nome == usuario):
    print('bom dia vinicius!')
elif (idade < 18):
    print('você é menor de idade!')
elif (idade > 100):
    print('está pessoa possivelmente não existe!')

