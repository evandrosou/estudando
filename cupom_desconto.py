valor_compra = float(input("Para calcular-mos o desconto,\nDigite o valor da compra!:"))
cod_cupom = input("Digite o código do cupom:")
desconto = 0
total = 0
# 'str.lower()' ou 'cod_cupom.lower() ou  foi usado para convertar a string para caixa baixa
# ou pode ser usado 'cod_cupom.upper()' deixando tudo em caixa alta
if str.lower(cod_cupom) == 'niver10':
    desconto = (valor_compra / 100) * 10
    total = valor_compra - desconto
    print("Valor a pagar é: {}".format(total))
else:
    print("Código incorreto!\nValor a pagar é: {}".format(valor_compra))
