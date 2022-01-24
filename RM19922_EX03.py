
numero = int(input("Digite um numero:"))
ant = 0
prox = 0
while prox < numero:
    print(prox)
    prox = prox + ant
    ant = prox - ant
    if (prox == 0):
        prox += 1
