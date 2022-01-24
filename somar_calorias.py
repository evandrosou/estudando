# algoritimos para soma calorica
# iniciando as variáveis
soma = 0
quantidade = 0
adicionar = input("Adicionar calorias? digite 'sim' ou 'não':")
#
while adicionar == 'sim':
    quantidade = int(input("Digite quantos alimentos foram ingeridos:"))
    for x in range(1,quantidade + 1):
        calorias = float(input("Digite as calorias do {}º alimento ingerido:".format(x)))
        soma = soma + calorias
    adicionar = input("Adicionar mais? digite 'sim' ou 'não':")
print("Total de calorias consumidas:{}".format(soma))