control = True
while control:

    n, m = map(int, input().split())

    if n <= 0 or m <= 0:
        break

    if m < n:
        n, m = m, n

    soma = 0
    lista = []
    for i in range(n, m+1):
        soma += i
        lista.append(i)

    print(*lista, end=" ")
    print(f"Sum={soma}")
