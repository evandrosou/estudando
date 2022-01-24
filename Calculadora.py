print("\nEsta é uma calculadora simples")
soma = 0
n1 = float(input("Digite um numero:"))
sinal = input("Digite o sinal de que quer usar:")
if sinal == 'x' or sinal == '*' or sinal == '-' or sinal == '/' or sinal == '+':
    n2 = float(input("Digite o outro numero:"))
    if sinal == '+':
        soma = n1 + n2
        print("O resultado é: {}".format(soma))
    elif sinal == '-':
        soma = n1 - n2
        print("O resultado é: {}".format(soma))
    elif sinal == '*':
        soma = n1 * n2
        print("O resultado é: {}".format(soma))
    elif sinal == 'x':
        soma = n1 * n2
        print("O resultado é: {}".format(soma))
    elif sinal == '/':
        if n1 >= n2:
            soma = n1 / n2
            print("O resultado é: {}".format(soma))
        else:
            soma = n2 / n1
            print("O resultado é: {}".format(soma))
    else:
        print("Sinal invalido")
else:
    print("Sinal inválido")
