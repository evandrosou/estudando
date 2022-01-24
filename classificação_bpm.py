print("Vamos verificar sue ritmo cardiaco!")
idade = int(input("Digite a sua idade:"))
bpm = int(input("Digite os batimentos por minuto:"))

if idade <= 2 :
    if bpm < 120:
        print("Seu batimento esta abaixo do adequado\nbatimento adequado esta entre 120 a 140!")
    elif bpm >= 120 and bpm <= 140:
        print("Seu batimento esta dentro do adequado")
    else:
        print("Seu batimento esta a cima do adequado\nbatimento adequado esta entre 120 a 140!")
elif idade >= 8 and idade <= 17:
    if bpm < 80:
        print("Seu batimento esta abaixo do adequado\nbatimento adequado esta entre 80 a 100!")
    elif bpm >= 80 and bpm <= 100:
        print("Seu batimento esta dentro do adequado")
    else:
        print("Seu batimento esta a cima do adequado\nbatimento adequado esta entre 80 a 100!")
elif idade >= 18 and idade <= 65:
    if bpm < 70:
        print("Seu batimento esta abaixo do adequado\nbatimento adequado esta entre 70 a 80!")
    elif bpm >= 70 and bpm <= 80:
        print("Seu batimento esta dentro do adequado")
    else:
        print("Seu batimento esta a cima do adequado\nbatimento adequado esta entre 70 a 80!")
elif idade > 65:
    if bpm < 50:
        print("Seu batimento esta abaixo do adequado\nbatimento adequado esta entre 50 a 60!")
    elif bpm >= 50 and bpm <= 60:
        print("Seu batimento esta dentro do adequado")
    else:
        print("Seu batimento esta a cima do adequado\nbatimento adequado esta entre 50 a 60!")
else:# abertura entre 2 anos a 7
    if bpm < 120:
        print("Seu batimento esta abaixo do adequado\nbatimento adequado esta entre 120 a 140!")
    elif bpm >= 120 and bpm <= 140:
        print("Seu batimento esta dentro do adequado")
    else:
        print("Seu batimento esta a cima do adequado\nbatimento adequado esta entre 120 a 140!")
