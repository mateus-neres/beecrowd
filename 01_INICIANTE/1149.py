valores = list(map(int, input().split()))

A = valores[0]

N = None
for valor in valores[1:]:
    if valor > 0:
        N = valor
        break

soma = sum(A + i for i in range(N))
print(soma)
