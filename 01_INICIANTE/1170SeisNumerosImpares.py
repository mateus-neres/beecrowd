entrada = int(input())

controle = 0
dado = entrada

while controle < 6:
    if dado % 2 == 1:
        print(dado)
        controle += 1
    dado +=1
