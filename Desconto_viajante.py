classe = input("Digite a classe desejada:")
viajantes = int(input("Informa quantas pessoas iram:"))
pacote = float(input("Informe o valor do pacote escolhido:"))
# iniciondo as variaveis do calculo
desconto = 0
media = 0
total = 0
if classe == 'economica':
    if viajantes != 0 and viajantes <= 2:
        desconto = pacote*0.03
        total = pacote - desconto
        media = total/viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
    elif  viajantes == 3:
        desconto = pacote * 0.04
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
    else:
        desconto = pacote * 0.05
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
elif classe == 'executiva':
    if viajantes != 0 and viajantes <= 2:
        desconto = pacote * 0.05
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
    elif viajantes == 3:
        desconto = pacote * 0.07
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
    else:
        desconto = pacote * 0.08
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
elif viajantes == 'primeira classe':
    if viajantes != 0 and viajantes <= 2:
        desconto = pacote * 0.10
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
    elif viajantes == 3:
        desconto = pacote * 0.15
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
    else:
        desconto = pacote * 0.20
        total = pacote - desconto
        media = total / viajantes
        print("\nCusto da viajem ${}".format(pacote))
        print("Desconto de ${}".format(desconto))
        print("Total a pagar é ${}".format(total))
        print("Custo por passageiro ${}".format(media))
else:
    print("Classe invalida!")