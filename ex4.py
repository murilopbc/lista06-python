idade = int(input("Digite a sua idade:"))

if idade < 16:
    print("Não eleitor")
elif idade < 18 or idade >= 70:
    print("Voto facultativo")
else:
    print("Voto obrigatório")
