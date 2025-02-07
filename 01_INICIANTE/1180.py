N = int(input())

X = list(map(int, input().split()))

menor_valor = X[0]
posicao = 0

for i in range(1, N):
    if X[i] < menor_valor:
        menor_valor = X[i]
        posicao = i

# Exibe o resultado
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
