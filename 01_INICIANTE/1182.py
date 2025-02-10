C = int(input())
T = input().strip()

M = []

for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    M.append(linha)

soma = 0
for i in range(12):
    soma += M[i][C]

if T == 'S':
    print(f"{soma:.1f}")
elif T == 'M':
    media = soma / 12
    print(f"{media:.1f}")
