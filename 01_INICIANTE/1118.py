control = True

while control:
    soma = 0
    cont = 0
    
    while cont < 2:
        n = float(input())
        if 0 <= n <= 10:
            soma += n
            cont += 1
        else:
            print("nota invalida")
    
    print(f"media = {soma / 2:.2f}")
    
    while True:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 1:
            break
        elif x == 2:
            control = False
            break
