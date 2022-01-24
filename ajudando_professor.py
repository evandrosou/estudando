print("\nVamos analizar sua nota!")
email_aluno = input("Digite seu e-mail:")

nota = input("Digite sua nota:")
# convertendo a nota:
nota = float(nota)
if nota > 8.5:
    print("Ótimo você foi aprovado!\nEnviando convite para: {}".format(email_aluno))


