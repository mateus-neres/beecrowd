control = True

while control:
    x, y = map(int, input().split())
    if x < y:
        print("Crescente")
    elif y < x:
        print("Decrescente")
    else:
        control = False
        