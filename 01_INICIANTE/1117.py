cont = 0
soma = 0
while True:
    n = float(input())

    if n >= 0 and n <= 10:
        soma += n
        cont += 1

    else:
        print("nota invalida")

    if cont == 2:
        break

media = soma / cont

print(f"media = {media:.2f}")
