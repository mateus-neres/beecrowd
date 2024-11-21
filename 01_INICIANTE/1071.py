a = int(input())
b = int(input())

if a > b:
    a, b = b, a

soma_impares = 0

for i in range(a + 1, b, 1):
    if i % 2 == 1:
        soma_impares += i

print(soma_impares)
