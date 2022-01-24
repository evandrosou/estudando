playstation = int(input("Digite os votos para o Playstation:"))
xbox = int(input("Digite os votos para o Xbox:"))
nintendo = int(input("Digite os votos para Nintendo:"))

if playstation > xbox and playstation > nintendo:
    print("\nO game mais votado é o Playstation com {} votos".format(playstation))
elif xbox > playstation and xbox > nintendo:
    print("\nO game mais votado é o Xbox com {} votos".format(xbox))
elif nintendo > playstation and nintendo > xbox:
    print("\nO game mais votado é o Nintendo com {} votos".format(nintendo))
