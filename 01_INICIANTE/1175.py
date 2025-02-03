N = []

for _ in range(20):
    X = int(input())
    N.append(X)

for i in range(len(N) // 2):
    N[i], N[len(N) - 1 - i] = N[len(N) - 1 - i], N[i]

for indice in range(len(N)):
    print(f"N[{indice}] = {N[indice]}")
