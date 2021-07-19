impar=0
for som in range(1, 501):
    if som % 2 != 0 and som % 3 == 0:
        impar += som
        print(f'{impar}')
        
        
        