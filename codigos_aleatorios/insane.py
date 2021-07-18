import time 
contagem = 10
print('O lançamento vai comecar...!')
for lançamento in range(contagem, 0, -1):
    print(f'{lançamento}')
    time.sleep(1)
print('FOGO!')