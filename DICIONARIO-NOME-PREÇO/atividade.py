produtos = {}

for i in range(5):
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    produtos[nome] = valor

valor_total = sum(produtos.values())

print("\nValor total da compra: R$", valor_total)