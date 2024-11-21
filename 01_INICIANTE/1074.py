qtd_entrada = int(input())

for i in range(qtd_entrada):
    entrada = int(input())
    if entrada == 0:
        print("NULL")
    elif entrada % 2 == 0 and entrada > 0:
        print("EVEN POSITIVE")
    elif entrada % 2 == 0 and entrada < 0:
        print("EVEN NEGATIVE")
    elif entrada % 2 != 0 and entrada > 0:
        print("ODD POSITIVE")
    elif entrada % 2 != 0 and entrada < 0:
        print("ODD NEGATIVE")