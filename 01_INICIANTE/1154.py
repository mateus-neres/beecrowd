N = int(input())

cont = 0
idade = 0

while N > 0:
    idade += N
    cont += 1

    N = int(input())

media = idade / cont

print(f"{media:.2f}")
