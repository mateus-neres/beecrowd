lista = []
for i in range(6):
    a = float(input())
    lista.append(a)

contador = 0
for i in lista:
    if i > 0:
        contador += 1

print(f'{contador} valores positivos')
