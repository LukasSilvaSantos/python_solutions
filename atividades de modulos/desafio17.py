              #calculo da hipotenusa.#
#Forma matematica de resolver.#
#catetoOposto = float(input('valor do cateto oposto: '))#
#catetoAdjacente = float(input('valor do cateto adjacente: '))#
#resposta = (catetoOposto**2 + catetoAdjacente**2) **(1/2)#
#print(f'A hipotenusa vai medir {resposta:.2f}')#
#resolução import biblioteca math, ou usar from impot math hypot para importar somente a hipotenusa.
import math
catetoOposto = float(input('valor do cateto oposto: '))
catetoAdjacente = float(input('valor do cateto adjacente: '))
resposta = math.hypot(catetoOposto, catetoAdjacente)
print(f'o valor da hipotenusa é {resposta:.2f}') 
