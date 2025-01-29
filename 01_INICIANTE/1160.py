T = int(input())

for _ in range(T):

    PA, PB, G1, G2 = map(float, input().split())
    PA = int(PA)
    PB = int(PB)

    cont_anos = 0


    while PA <= PB and cont_anos <= 100:

        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        cont_anos += 1


    if cont_anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{cont_anos} anos.")
