n = int(input())

for i in range(n):
    soma_impares = 0
    x, y = map(int, input().split())
    if y < x:
        for j in range(y+1, x):
            if j % 2 == 1:
                soma_impares += j
    else:
        for j in range(x+1, y):
            if j % 2 == 1:
                soma_impares += j
    print(soma_impares)