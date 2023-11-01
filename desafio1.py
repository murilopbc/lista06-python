import random
chance = 2
num_certo = random.randint(0, 10)
print(num_certo)
palpite = int(input("Digite um número de 0 a 10:"))

if palpite == num_certo:
    print("Parabéns, você acertou!")
elif palpite != num_certo:
    print("Você errou. Tente outra vez!")
    if palpite < num_certo:
        print("Dica: É um número maior!")
    else:
        print("Dica: É um número menor!")
    palpite = int(input("Digite um número de 0 a 10:"))
    if palpite == num_certo:
        print("Parabéns, você acertou!")
    else:
        print("Você perdeu!")
