idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))

maior_idade = 0
menor_idade = 0

if idade1 > idade2 and idade1 > idade3:
    maior_idade = idade1
elif idade2 > idade1 and idade2 > idade3:
    maior_idade = idade2
else:
    maior_idade = idade3

if idade1 < idade2 and idade1 < idade3:
    menor_idade = idade1
elif idade2 < idade1 and idade2 < idade3:
    menor_idade = idade2
else:
    menor_idade = idade3

print(f"A maior idade é: {maior_idade}")
print(f"A menor idade é: {menor_idade}")
