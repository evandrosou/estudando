segunda = int(input("Digite os votos para segunda-feira:"))
terca = int(input("Digite os votos para terça-feira:"))
quarta = int(input("Digite os votos para quarta-feira:"))
quinta = int(input("Digite os votos para quinta-feira:"))
sexta = int(input("Digite os votos para sexta-feira:"))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("\nO dia mais votado é segunda com {} votos".format(segunda))
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("\nO dia mais votado é terça com {} votos".format(terca))
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("\nO dia mais votado é quarta com {} votos".format(quarta))
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("\nO dia mais votado é quinta com {} votos".format(quinta))
else:
    print("\nO dia mais votado é sexta com {} votos".format(sexta))
