X = int(input())

cont = 1
soma = X

while True:
    Z = int(input())

    if Z > X:
        break


for i in range(X, Z):
    soma += i
    cont += 1

    if soma > Z:
        break

print(cont)
