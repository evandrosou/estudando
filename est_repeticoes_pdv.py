# simulando sistema Ponto de venda
# criando variavel para somar valor da compra usando while
'''soma = 0
# variavel que recebe o valor
item = int(input("Digite o valor do item:"))
# estrutura de repetição enquanto item tiver valor continuara
while item != 0:
    soma = soma + item
    item = int(input("Digite o valor do item:"))
# final da estrutura imprimir soma total
print("Compra total $:{}".format(soma))


# usando for para outro exemplo clculando mádia
quant = int(input("Informe a quantidade de alunos:"))
# iniciando a variavel soma para somar média
soma = 0
# 'c' é o contador e 'range' limite das vezes
for c in range(quant):
    nota = float(input("Digite a nota do aluno:"))
    soma = soma + nota
# calculo da média
media = soma / quant
print("O calculo da média é:{}".format(media))'''


# conversão de fahrenheit para centígrados
'''f = 50
celsius = 0
while f <= 150:
    celsius = (f - 32)* 5/9
    print("Fahrenheit: {}, Celsius: {:.2F}".format(f,celsius))
    f = f + 1'''

# somando as repetições
soma = 0
n = int(input("Informe o valor de n:"))
for x in range(1,n+1):
    print(x)

