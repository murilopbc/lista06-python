while True:
    print("Operações")
    print("1 - soma")
    print("2 - subtração")
    print("3 - divisão")
    print("4 - multiplicação")
    print("5 - sair")

    opcao = int(input("Selecione uma opção: "))

    if opcao >= 5:
        print("Sair")
        break

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um outro número: "))

    if opcao == 1:
        print("Resultado:", num1 + num2)
    elif opcao == 2:
        print("Resultado:", num1 - num2)
    elif opcao == 3:
        print("Resultado:", num1 / num2)
    else:
        print("Resultado:", num1 * num2)
