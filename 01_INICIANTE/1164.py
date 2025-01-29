N = int(input())

for _ in range(N):
    X = int(input())

    divisores = []

    for i in range(1, X):
        if X % i == 0:
            divisores.append(i)
    
    sum = 0
    for item in divisores:
        sum += item

    if sum == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
        