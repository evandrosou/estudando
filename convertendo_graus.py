# exercicio 03 - convertendo graus celsius para fahrenheit
# definindo a função para calcular a conversão
def calc_celcius(fah):
    cel = 5 / 9 * (fah - 32)
    return cel


for fah in range(50, 150 + 1):
    # repassando o valor para a função
    calc_celcius(fah)
    # na função a variavel 'fah' retorna com o valor de 'cel'
    print("{} : {:.1f}".format(fah, calc_celcius(fah)))
