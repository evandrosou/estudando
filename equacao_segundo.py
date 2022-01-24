
import math
# importando classe para calcular a raiz de um numero

print("Digite os valores a baixo")
a = float(input("Digite o valor de 'A':"))
b = float(input("Digite o valor de 'B':"))
c = float(input("Digite o valor de 'C':"))
x1 = 0
x2 = 0
x = 0
delta = b * b - 4 * a * c
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} + 0,os valores são: x1 = {} e x2 = {}".format(a,b,c,x1,x2))
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x² + {}x + {} + 0,os valores são: x =  {}".format(a, b, c, x))
else:
    print("Para a equação {}x² + {}x + {} + 0, não existem valores reais para x".format(a, b, c,))
print(delta)
