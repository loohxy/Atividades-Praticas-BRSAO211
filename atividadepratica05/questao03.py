def calcular_desconto(valor_produto, porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    valor_final = valor_produto - desconto
    return valor_final

valor_produto = float(input("Digite o valor do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

desconto = calcular_desconto(valor_produto, porcentagem_desconto)

print(f"O valor do desconto é de: {desconto:.2f}")
