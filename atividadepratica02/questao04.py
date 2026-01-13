distancia_percorrida = float(input("Digite a distância percorrida em KM: "))
combustivel_gasto = float(input("Digite o combustível gasto em litros: "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"consumo médio: {consumo_medio:.2f}")
print(f"Distância: {distancia_percorrida} KM/L")
print(f"combustível gasto: {combustivel_gasto} L")
