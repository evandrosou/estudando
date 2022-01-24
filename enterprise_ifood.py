# armazenando valores dos restaurantes nas listas
mineiro = ('O Mineiro','Brasileira','30-40 min','Grátis',4.2,1.7)
amor_pedacos = ('Amor aos pedaços','Doces e Bolos','46-56 min','R$ 5,99',4.3,1.2)
we_coffee = ('We Coffee','Cafeteria','45-55 min','R$ 4,49',4.5,0.8)
kazu = ('Lamen Kazu - Liberdade','Japonesa','31-41 min','R$ 6,99',4.6,0.7)
pretzels = ('Mr. Pretzels','Lanches','45-55 min','R$ 4,99',4.7,1.1)
brigaderia = ('Brigaderia Shopping Paulista','Doces e Bolos','41-51 min','R$ 5,99',4.7,1.2)
restaurantes = [mineiro,amor_pedacos,we_coffee,kazu,pretzels,brigaderia]
classificacao = []
# funções
def imprimir(rest):
    print("{}\n{} * {} * {}Km\n{} * {}".format(rest[0],rest[-2],rest[1],rest[-1],rest[2],rest[4]))
    return
def armazenar(list):
    classificacao.append(list)



# menu para escolha
print("Escolha o restaurante mais proximo de você!!")
opcao = int(input("Digite uma das opições a baixo:\n 1 - Ver restaurantes por pontuação!\n 2 - Ver restaurantes por distância!\n 3 - Deixe a indicação por nossa conta!!\n-->:"))
if opcao == 1:
    for x in restaurantes:#[mineiro,amor_pedacos,we_coffee,kazu,pretzels,brigaderia]
        if x[-2] >= 4.5:
            armazenar(x)
            imprimir(classificacao)








