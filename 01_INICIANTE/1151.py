N = int(input())

lista = [0,1]

for i in range(2, N):
    lista.append(lista[-1] + lista[-2])

print(" ".join(map(str, lista)))
