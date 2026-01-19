import datetime

def caulcula_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual -ano_nascimento
    return idade * 365

ano_nascimento = float(input("Digite o ano de nascimento: "))

dias_vividos = caulcula_idade(ano_nascimento)

print(f"Você tem {dias_vividos} dias vividos")