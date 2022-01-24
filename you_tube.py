# iniciando a variável
bonus = 0
a_pagar = 0
assinatura = input("Digite a assinatura do cliente:")
# condição para iniciaro algoritimo:
if str.lower(assinatura) == 'basic' or str.lower(assinatura) == 'silver' or str.lower(assinatura) == 'gold' or str.lower(assinatura) == 'platinum':
    faturamento = float(input("Digite o faturamento anual do cliente:"))
    # Desvios por classificação:
    if str.lower(assinatura) == 'basic':
        bonus = (faturamento/100)* 30
        a_pagar = faturamento - bonus
        print("\nCliente: {}".format(assinatura))
        print("Desconto de: ${:.2f}".format(bonus))
        print("Valor a receber é: ${:.2f}".format(a_pagar))
    elif str.lower(assinatura) == 'silver':
        bonus = (faturamento / 100) * 20
        a_pagar = faturamento - bonus
        print("\nCliente: {}".format(assinatura))
        print("Desconto de: ${:.2f}".format(bonus))
        print("Valor a receber é: ${:.2f}".format(a_pagar))
    elif str.lower(assinatura) == 'gold':
        bonus = (faturamento / 100) * 10
        a_pagar = faturamento - bonus
        print("\nCliente: {}".format(assinatura))
        print("Desconto de: ${:.2f}".format(bonus))
        print("Valor a receber é: ${:.2f}".format(a_pagar))
    else:# classificação platinum:
        bonus = (faturamento / 100) * 5
        a_pagar = faturamento - bonus
        print("\nCliente: {}".format(assinatura))
        print("Desconto de: ${:.2f}".format(bonus))
        print("Valor a receber é: ${:.2f}".format(a_pagar))
else:
    print("assinatura incorreta!")