N = int(input())

for a in range(N):
    X, Y = map(int, input().split())

    sum = 0
    cont = 0
    while cont < Y:
        
        if X % 2 == 1:
            cont += 1
            sum += X
        
        X += 1

    print(sum)
