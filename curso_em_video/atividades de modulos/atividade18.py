#calcular seno, cosseno e tangente
#pode calcular importando a biblioteca MATH ou usando o from import math radians(radiante), sin(seno), cos(cosseno), tan(tangente) 
import math
ângulo = float(input('Qual o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print(f' O ângulo é {ângulo}. \n o seu seno é {seno:.2f}. \n o seu cosseno é {cosseno:.2f}. \n e a sua tangente é {tangente:.2f}')
