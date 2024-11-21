CONSUMO = 12

tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade

consumo = distancia / CONSUMO

print(f"{consumo:.3f}")
