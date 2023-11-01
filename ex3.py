quantidade_produto = int(input("Digite a quantidade de produto adquirido: "))
preco_produto = float(input("Digite o valor unitário do produto: "))
valor_do_desconto = preco_produto * 0.10
valor_desconto = preco_produto * 0.05

if quantidade_produto > 100:

    desconto_unidade = preco_produto * 0.1
    valor_final = quantidade_produto * preco_produto * 0.9

    print("O valor inicial é: ", preco_produto)
    print("A quantidade solicitada é: ", quantidade_produto)
    print("O valor unitário de desconto é: ", desconto_unidade)
    print("O valor final é: ", valor_final)
else:
    desconto_unidade = preco_produto * 0.05
    valor_final = quantidade_produto * preco_produto * 0.95

    print("O valor inicial é: ", preco_produto)
    print("A quantidade solicitada é: ", quantidade_produto)
    print("O valor unitário de desconto é: ", desconto_unidade)
    print("O valor final é: ", valor_final)
