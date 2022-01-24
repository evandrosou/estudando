# exercicio 02 - média de notas da sala
notas = 0
cont = 1
acm = 0
quant_aluno = int(input("Digite a quantidade de alunos:"))
while cont <= quant_aluno:
    notas = float(input("Digite a nota do {}° aluno:".format(cont)))
    acm = acm + notas
    cont +=1
media = acm / cont
print("Essa é a média: {}".format(media))