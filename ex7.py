nota_prova = float(input("Digite a nota da prova: "))

if nota_prova > 10:
    print("Nota inválida")
elif nota_prova >= 9:
    print("A")
elif nota_prova >= 7:
    print("B")
elif nota_prova >= 5:
    print("C")
elif nota_prova >= 3:
    print("D")
else:
    print("E")
