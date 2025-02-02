vetor = []
for i in range(10):
    X = int(input())

    if X <= 0:
        X = 1

    vetor.append(X)

    print(f'X[{i}] = {vetor[i]}')
