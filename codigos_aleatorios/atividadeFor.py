resultado = 0
for soma in range(1, 5001):
    if (soma%3 == 0 and soma%2 != 0):
        resultado += soma
print(resultado)