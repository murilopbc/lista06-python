prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))
prova3 = float(input("Digite a nota da terceira prova: "))

if prova1 < prova2 and prova1 < prova3:
    media = (prova2 + prova3) / 2
    print("A média é: ", media)
elif prova2 < prova1 and prova2 < prova3:
    media = (prova1 + prova3) / 2
    print("A média é:", media)
else:
    media = (prova1 + prova2) / 2
    print("A média é: ", media)
