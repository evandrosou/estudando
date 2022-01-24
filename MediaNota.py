def entrada_nota():
    nota = float(input("Informe o valor da nota: "))
    return nota

def media_nota(n,c):
    n = n / c
    return n

nota = 0
cont = 0
inicio = input("adicionar nota? 'sim ou 'não':")
while inicio == 'sim':
    n = entrada_nota()
    inicio = input("Incluir novamente?:")
    nota = nota + n
    cont = cont +1

media_final = media_nota(nota,cont)

#verificação
if media_final >= 7.0:
    print("A média %.1f - Aprovado"% media_final)
else:
    print("A média {} - Reprovado".format(media_final))