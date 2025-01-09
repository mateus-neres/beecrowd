lista = []
for i in range(100):
    entrada = int(input())
    lista.append(entrada)

maior = lista[0]
for i in range(len(lista)):
    if lista[i] >= maior:
        maior = lista[i]

print(f"{maior}\n{lista.index(maior)+1}")
