# exercicio 01 - somador
#baseado em um sistema de caixa de mercado, vai acumulando os valores
acm = 0
num = float(input("Digite um numero:"))
while num != 0:
    acm = acm + num
    num = float(input("Digite um numero:"))
print('Total da compra: $ {.:2f}'.format(acm))