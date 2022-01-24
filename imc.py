print("\nVamos calcular seu indice de massa corpórea!")
peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))
# formula para o calculo do imc:
imc = peso/(altura * altura)
# Desvios para classificação de peso
if imc < 16.00:
    print("Seu IMC é: {:.2f}\nBaixo peso 3º grau".format(imc))
elif imc >= 16.00 and imc <= 16.99:
    print("Seu IMC é: {:.2f}\nBaixo peso 2º grau".format(imc))
elif imc >= 17.00 and imc <= 18.49:
    print("Seu IMC é: {:.2f}\nBaixo peso 1º grau".format(imc))
elif imc >= 18.50 and imc <= 24.99:
    print("Seu IMC é: {:.2f}\nPeso ideal!".format(imc))
elif imc >= 25.00 and imc <= 29.99:
    print("Seu IMC é: {:.2f}\nSobrepeso".format(imc))
elif imc >= 30.00 and imc <= 34.99:
    print("Seu IMC é: {:.2f}\nObesidade 1º grau".format(imc))
elif imc >= 35.00 and imc <= 39.99:
    print("Seu IMC é: {:.2f}\nObesidade 2º grau".format(imc))
else :
    print("Seu IMC é: {:.2f}\nObesidade 3º grau".format(imc))