peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura*altura)
if imc < 18.5:
    print(f"Baixo peso", "{:.2f}".format(imc))
elif imc <= 24.9:
    print(f"Normal", "{:.2f}".format(imc))
elif imc <= 29.9:
    print(f"Sobrepeso", "{:.2f}".format(imc))
elif imc <= 34.9:
    print(f"Obesidade", "{:.2f}" .format(imc))
elif imc <= 39.9:
    print("Obesidade Mórbida", "{:.2f}".format(imc))
else:
    print("Obesidade grau 3", "{:.2f}".format(imc))
