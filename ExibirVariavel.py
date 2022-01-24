codigo = 105
nome = 'José Santana'
salario = 1650.00
ativo = True

#metodos para imprimir
print("Código %d" % codigo)
print("nome: %s"% nome)
print("Salario: %.2f"% salario)
print("Situação: %r"% ativo)
print("-----------------------------------")

#segunda forma de imprimir
print("Código: {}".format(codigo))
print("nome: {}".format(nome))
print("Salario: {:.2f}".format(salario))
print("Situação: {}".format(ativo))

