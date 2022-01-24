# iniciando as variáveis
soma = 0
quantidade = 0
media = 0
adicionar = input("Adicionar gastos? digite 'sim' ou 'não':")
# estrutura de repetição com controle
while adicionar == 'sim':
    quantidade = int(input("Digite a quantidade de despesas:"))
    for x in range(1,quantidade + 1):
        despesa = float(input("Digite valor da {}º despesa:".format(x)))
        soma = soma + despesa
        media = soma / quantidade
print("Total dos valores gastos: ${}".format(soma))
print("Média por valor gasto: ${}".format(media))