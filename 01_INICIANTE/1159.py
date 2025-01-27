N = int(input())

while N != 0:

    cont = 1
    sum = 0

    while cont <= 5:
        if N % 2 == 0:
            cont += 1
            sum += N
        N += 1    

    print(sum)

    N = int(input())
