n = int(input())
lista = []
control = 1
cont = 0
for i in range(n):

    while control <= 3:
        lista.append(i + control + cont)
        control += 1

    print(" ".join(map(str, lista)), end="")
    print(" PUM")
    lista = []
    control = 1
    cont += 3
    